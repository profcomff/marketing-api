from fastapi import APIRouter
from fastapi_sqlalchemy import db
from sqlalchemy.exc import SQLAlchemyError

from .models import ActionInfo
from ..exceptions import DB_Error
from ..models.db import ActionsInfo

action_router = APIRouter(prefix='/action', tags=['user_actions'])


@action_router.post('/v1/action')
def write_action(user_action_info: ActionInfo):
    try:
        db.session.add(ActionsInfo(**user_action_info.dict()))
        db.session.flush()
    except SQLAlchemyError:
        raise DB_Error
