import sqlalchemy
from fastapi import APIRouter
from .models import ActionInfo
from fastapi_sqlalchemy import db
from sqlalchemy.exc import SQLAlchemyError
from marketing_api.methods.db_utils import add_action_from_user_info

action_router = APIRouter(prefix='/action', tags=['user_actions'])


@action_router.post('/v1/post')
def write_action(user_action_info: ActionInfo):
    add_action_from_user_info(user_action_info, db.session)
