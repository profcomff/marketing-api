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
    additional_data = Column(sqlalchemy.String, nullable=True)
    create_ts = Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"ActionInfo(user_id: {self.user_id}, action: {self.action}"


class User(Base):
    id = Column(sqlalchemy.Integer, primary_key=True)
    union_number = Column(sqlalchemy.String, nullable=True)
    modify_ts = Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    create_ts = Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User(id: {self.id}, union_number: {self.union_number}"
