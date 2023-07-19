from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class ActionInfo(Base):
    user_id: int | None = None
    action: str
    additional_data: str | None = None
    path_from: str | None = None
    path_to: str | None = None


class User(Base):
    id: int
    union_number: str | None = None


class UserPatch(Base):
    union_number: str | None = None
    auth_user_id: int | None = None
