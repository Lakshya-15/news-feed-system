from sqlalchemy import Column, Integer
from app.db.base import Base

class Follow(Base):
    __tablename__ = "follows"

    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer)
    followee_id = Column(Integer)