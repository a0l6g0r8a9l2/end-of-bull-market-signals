from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class Channel(Base):
    __tablename__ = "yt_crypto_channels"

    id = Column(Integer, primary_key=True, index=True)
    channel_id = Column(String, nullable=False)
    channel_title = Column(String)
    view_count = Column(Integer, nullable=False)
    subscriber_count = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)