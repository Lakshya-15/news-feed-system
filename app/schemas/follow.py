from pydantic import BaseModel


class FollowCreate(BaseModel):
    follower_id: int
    followee_id: int


class FollowOut(BaseModel):
    message: str
