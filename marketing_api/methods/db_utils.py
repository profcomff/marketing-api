import datetime
from sqlalchemy.orm import Session
from marketing_api import exceptions
from marketing_api.models.db import ActionsInfo
from marketing_api.routes.action import ActionInfo
from sqlalchemy.exc import SQLAlchemyError
from marketing_api.exceptions import DB_Error


def add_action_from_user_info(user_info: ActionInfo,
                              session: Session) -> None:
    try:
        session.add(ActionsInfo(**user_info.dict()))
        session.flush()
    except SQLAlchemyError:
        raise DB_Error
