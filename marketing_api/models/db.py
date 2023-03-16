import enum
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy import Column

from .base import Base


class Actions(str, enum.Enum):
    LOGGED_IN: str = "logged_in"
    LOGGED_OUT: str = "logged_out"
    AUTHORIZED: str = "authorized"
    INSTALLED: str = "installed"


class User(Base):
    id = Column(sa.Integer, primary_key=True)
    union_number = Column(sa.String, nullable=True)
    auth_user_id = Column(sa.Integer, nullable=True)
    modify_ts = Column(sa.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    create_ts = Column(sa.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User(id={self.id}, union_number={self.union_number}, auth_user_id={self.auth_user_id})"


class ActionsInfo(Base):
    """Actions from user"""

    id = Column(sa.Integer, primary_key=True)
    user_id = Column(sa.Integer)
    action = Column(sa.String, nullable=False)
    path_from = Column(sa.String, nullable=False)
    path_to = Column(sa.String, nullable=True)
    additional_data = Column(sa.String, nullable=True)
    create_ts = Column(sa.DateTime, nullable=False, default=datetime.utcnow)

    user = relationship(User, primaryjoin="foreign(ActionsInfo.user_id)==User.id", uselist=False)

    def __repr__(self):
        return f"ActionInfo(user_id={self.user_id}, action={self.action})"
