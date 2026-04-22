from fastapi import FastAPI
from app.api.routes import users, posts, follows
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="News Feed System")

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(follows.router)

@app.get("/")
def root():
    return {"message": "API is running"}




