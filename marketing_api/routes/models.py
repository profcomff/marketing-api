from pydantic import BaseModel, AnyHttpUrl


class Base(BaseModel):
    class Config:
        orm_mode = True


class ActionInfo(Base):
    user_key: str
    action: str
    path_from: AnyHttpUrl
    path_to: AnyHttpUrl | None

