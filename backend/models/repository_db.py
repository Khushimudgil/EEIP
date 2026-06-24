from sqlalchemy import Column, Integer, String

from database.database import Base


class RepositoryDB(Base):

    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)

    repo_url = Column(String)

    status = Column(String)