from fastapi import APIRouter
from fastapi_sqlalchemy import db
from starlette.responses import PlainTextResponse

from .models import ActionInfo
from ..models.db import ActionsInfo

action_router = APIRouter(prefix='/action', tags=['User Action'])


@action_router.post('/v1/action')
def write_action(user_action_info: ActionInfo):
    db.session.add(ActionsInfo(**user_action_info.dict()))
    db.session.flush()
    return PlainTextResponse(status_code=204)
