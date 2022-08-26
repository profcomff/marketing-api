import datetime
from sqlalchemy.orm import Session
from engine import exceptions
from engine.models.db import ActionsInfo
from engine.routes.action import ActionInfo
from sqlalchemy.exc import SQLAlchemyError
from engine.exceptions import DB_Error


def add_action_from_user_info(user_info: ActionInfo,
                              session: Session) -> None:
    try:
        session.add(ActionsInfo(**user_info.dict()))
        session.flush()
    except SQLAlchemyError:
        raise DB_Error
