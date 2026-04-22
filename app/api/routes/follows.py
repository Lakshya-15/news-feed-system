from fastapi import APIRouter
from app.db.session import SessionLocal
from app.models.follow import Follow

router = APIRouter(prefix="/follows", tags=["Follows"])


@router.post("/")
def follow_user(follower_id: int, followee_id: int):
    db = SessionLocal()
    follow = Follow(follower_id=follower_id, followee_id=followee_id)
    db.add(follow)
    db.commit()
    return {"message": "Followed successfully"}