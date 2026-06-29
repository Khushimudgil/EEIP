from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database.database import Base


class ChatHistoryDB(Base):

    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    repo_id = Column(Integer)

    question = Column(String)

    answer = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )