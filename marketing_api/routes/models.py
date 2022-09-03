from pydantic import BaseModel, AnyHttpUrl


class Base(BaseModel):
    class Config:
        orm_mode = True


class ActionInfo(Base):
    user_id: int
    action: str
    path_from: str | None
    path_to: str | None


class User(Base):
    id: int
