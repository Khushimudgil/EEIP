from database.database import SessionLocal
from models.repository_metadata_db import RepositoryMetadataDB


def save_metadata(repo_id, metadata):

    db = SessionLocal()

    for file_data in metadata:

        metadata_row = RepositoryMetadataDB(
            repo_id=repo_id,
            file_name=file_data.get("file", ""),
            language=file_data.get("language", ""),
            classes=str(file_data.get("classes", [])),
            functions=str(file_data.get("functions", [])),
            methods=str(file_data.get("methods", [])),
            imports=str(file_data.get("imports", []))
        )

        db.add(metadata_row)

    db.commit()
    db.close()