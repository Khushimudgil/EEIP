from database.database import SessionLocal
from models.repository_db import RepositoryDB


def get_repository_status(
    repo_id: int
):

    db = SessionLocal()

    repo = (
        db.query(RepositoryDB)
        .filter(
            RepositoryDB.id == repo_id
        )
        .first()
    )

    db.close()

    if not repo:
        return None

    return repo.status