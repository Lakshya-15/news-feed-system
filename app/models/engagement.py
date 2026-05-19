from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.db.base import Base


class Engagement(Base):
    __tablename__ = "engagements"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    post_id = Column(Integer, nullable=False)
    action = Column(String, nullable=False)  # "like" or "click"
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
