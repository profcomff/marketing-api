import logging
from typing import Annotated

from auth_lib.fastapi import UnionAuth
from fastapi import Depends, FastAPI, Header
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware, db
from pydantic import ValidationError
from starlette.responses import PlainTextResponse

from marketing_api import __version__
from marketing_api.models import ActionsInfo
from marketing_api.models.db import User as DbUser
from marketing_api.settings import get_settings

from .models import ActionInfo, User, UserPatch


settings = get_settings()
logger = logging.getLogger(__name__)
app = FastAPI(
    title='Сервис мониторинга активности пользователей',
    description='API для проведения маркетинговых исследований',
    version=__version__,
    # Настраиваем интернет документацию
    root_path=settings.ROOT_PATH if __version__ != 'dev' else '/',
    docs_url=None if __version__ != 'dev' else '/docs',
    redoc_url=None,
)


@app.post('/v1/action')
async def write_action(
    user_action_info: ActionInfo,
    user=Depends(UnionAuth(auto_error=False, allow_none=True)),
    user_agent: Annotated[str | None, Header()] = None,
):
    """Создать действие"""
    user_id = user.get("id") if user else None
    logger.debug(f"write_action by {user_id=}")
    ai = ActionsInfo(**user_action_info.dict())
    db.session.add(ai)
    db.session.flush()
    if ai.user:
        logger.debug(ai.user)
        ai.user.auth_user_id = user_id
        ai.user.user_agent = user_agent
        db.session.flush()
    else:
        logger.warning(f"write_action with user {user_action_info.user_id} not exists!")
    return PlainTextResponse(status_code=200)


@app.post('/v1/user', response_model=User)
async def create_user(user=Depends(UnionAuth(auto_error=False, allow_none=True))):
    """Создать уникальный идентификатор установки"""
    user_id = user.get("id") if user else None
    logger.debug(f"create_user by {user_id=}")
    dbuser = DbUser()
    dbuser.auth_user_id = user.get("id") if user else None
    db.session.add(dbuser)
    db.session.flush()
    return dbuser


@app.patch('/v1/user/{id}', response_model=User)
async def patch_user(id: int, patched_user: UserPatch, user=Depends(UnionAuth(["marketing.user.patch"]))):
    """Изменить пользователя в маркетинге

    Необходимые scopes: `marketing.user.patch`
    """
    user_id = user.get("id") if user else None
    logger.debug(f"patch_user by {user_id=}")
    result: DbUser = db.session.query(DbUser).filter(DbUser.id == id).one_or_none()
    if not result:
        raise HTTPException(404, "No user found")
    if patched_user.union_number:
        result.union_number = patched_user.union_number
    if patched_user.auth_user_id:
        result.union_number = patched_user.auth_user_id
    db.session.flush()
    return result


@app.exception_handler(ValidationError)
async def http_validation_error_handler(req, exc):
    return PlainTextResponse("Invalid data", status_code=422)


@app.exception_handler(Exception)
async def http_error_handler(req, exc):
    return PlainTextResponse("Error", status_code=500)


app.add_middleware(
    DBSessionMiddleware,
    db_url=settings.DB_DSN,
    engine_args={"pool_pre_ping": True, "isolation_level": "AUTOCOMMIT"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)
