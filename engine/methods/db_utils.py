import datetime
from sqlalchemy.orm import Session
from engine import exceptions
from engine.models.db import ActionsInfo
from engine.routes.action import ActionInfo


def add_action_from_user_info(user_info: ActionInfo,
                              session: Session) -> None:
    session.add(ActionsInfo(
        user_key=user_info.user_key,
        action=user_info.action,
        path_from=user_info.path_from,
        path_to=user_info.path_to)
    )
    session.flush()