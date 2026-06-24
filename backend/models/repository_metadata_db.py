from sqlalchemy import Column, Integer, String, ForeignKey

from database.database import Base


class RepositoryMetadataDB(Base):

    __tablename__ = "repository_metadata"

    id = Column(Integer, primary_key=True, index=True)

    repo_id = Column(Integer, ForeignKey("repositories.id"))

    file_name = Column(String)

    language = Column(String)

    classes = Column(String)

    functions = Column(String)

    methods = Column(String)

    imports = Column(String)