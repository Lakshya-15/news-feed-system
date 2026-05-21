from pydantic import BaseModel, ConfigDict
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: str | None = None


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str | None
    created_at: datetime
