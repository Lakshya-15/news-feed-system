from pydantic import BaseModel, ConfigDict
from datetime import datetime


class PostCreate(BaseModel):
    author_id: int
    content: str


class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    author_id: int
    content: str
    likes_count: int
    created_at: datetime
