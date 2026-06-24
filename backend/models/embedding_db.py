from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text

from database.database import Base


class EmbeddingDB(Base):

    __tablename__ = "embeddings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    content = Column(Text)

    embedding = Column(Text)