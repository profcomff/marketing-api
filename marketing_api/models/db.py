from datetime import datetime
import sqlalchemy.orm
from sqlalchemy import Column
from .base import Base
import enum


class Actions(str, enum.Enum):
    LOGGED_IN: str = "logged_in"
    LOGGED_OUT: str = "logged_out"
    AUTHORIZED: str = "authorized"
    INSTALLED: str = "installed"


class ActionsInfo(Base):
    """Actions from user"""

    id = Column(sqlalchemy.Integer, primary_key=True)
    user_id = Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    action = Column(sqlalchemy.String, nullable=False)
    path_from = Column(sqlalchemy.String, nullable=False)
    path_to = Column(sqlalchemy.String, nullable=True)
    create_ts = Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"ActionInfo(user_key: {self.user_key}, action: {self.action}"


class User(Base):
    id = Column(sqlalchemy.Integer, primary_key=True)
