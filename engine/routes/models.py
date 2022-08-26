import datetime
from pydantic import BaseModel, AnyHttpUrl, validator
from engine.models.db import Actions
from engine.exceptions import ActionError


class Base(BaseModel):
    class Config:
        orm_mode = True


class ActionInfo(Base):
    user_key: str
    action: str
    path_from: AnyHttpUrl
    path_to: AnyHttpUrl | None

    @classmethod
    @validator('action')
    def print(cls, value):
        if value not in [a.name for a in Actions]:
            raise ValueError(f"Invalid action {value}")
