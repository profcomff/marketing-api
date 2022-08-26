from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from starlette.responses import PlainTextResponse

from marketing_api import get_settings
from marketing_api.models import ActionsInfo
from .models import ActionInfo, User
from marketing_api.models.db import User as DbUser

settings = get_settings()
app = FastAPI()


@app.post('/v1/action')
async def write_action(user_action_info: ActionInfo):
    db.session.add(ActionsInfo(**user_action_info.dict()))
    db.session.flush()
    return PlainTextResponse(status_code=204)


@app.post('/v1/user', response_model=User)
async def create_user():
    user = DbUser()
    db.session.add(user)
    db.session.flush()
    return user




@app.exception_handler(Exception)
def http_sqlalchemy_error_handler():
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
