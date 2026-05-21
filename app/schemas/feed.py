from pydantic import BaseModel
from app.schemas.post import PostOut


class FeedResponse(BaseModel):
    posts: list[PostOut]
    next_cursor: float | None = None
