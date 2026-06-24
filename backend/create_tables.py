from database.database import engine
from models.repository_db import RepositoryDB
from database.database import Base
from models.repository_metadata_db import RepositoryMetadataDB
from models.embedding_db import EmbeddingDB

Base.metadata.create_all(bind=engine)

print("Tables Created Successfully!")