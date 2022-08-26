import datetime
from pydantic import BaseModel, AnyHttpUrl, validator
from marketing_api.models.db import Actions
from marketing_api.exceptions import ActionError


class Base(BaseModel):
    class Config:
        orm_mode = True


class ActionInfo(Base):
    user_key: str
    action: str
    path_from: AnyHttpUrl
    path_to: AnyHttpUrl | None

