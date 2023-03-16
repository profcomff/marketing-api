from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        orm_mode = True


class ActionInfo(Base):
    user_id: int | None
    action: str
    additional_data: str | None
    path_from: str
    path_to: str | None


class User(Base):
    id: int
    union_number: str | None


class UserPatch(Base):
    union_number: str
