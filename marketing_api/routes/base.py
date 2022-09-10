from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.exceptions import HTTPException
from fastapi_sqlalchemy import db
from starlette.responses import PlainTextResponse
from sqlalchemy.exc import IntegrityError
import starlette
from marketing_api import get_settings
from marketing_api.models import ActionsInfo
from .models import ActionInfo, User
from marketing_api.models.db import User as DbUser
from pydantic import ValidationError

settings = get_settings()
app = FastAPI()


@app.post('/v1/action')
async def write_action(user_action_info: ActionInfo):
    db.session.add(ActionsInfo(**user_action_info.dict()))
    db.session.flush()
    return PlainTextResponse(status_code=200)


@app.post('/v1/user', response_model=User)
async def create_user():
    user = DbUser()
    db.session.add(user)
    db.session.flush()
    return user


@app.patch('/v1/user/{id}', response_model=User)
async def patch_user(id: int, union_number: int):
    result: DbUser = db.session.query(DbUser).filter(DbUser.id == id).one_or_none()
    if not result:
        raise HTTPException(404, "No user found")
    result.union_number = union_number
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
    session_args={"autocommit": True},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)
