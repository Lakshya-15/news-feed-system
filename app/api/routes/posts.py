from fastapi import APIRouter
from app.db.session import SessionLocal
from app.models.post import Post

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/")
def create_post(author_id: int, content: str):
    db = SessionLocal()
    post = Post(author_id=author_id, content=content)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post