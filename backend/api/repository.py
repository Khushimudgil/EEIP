from unittest import result

from fastapi import APIRouter

from models.repository import RepositoryRequest
from models.repository_db import RepositoryDB
from models.status import RepositoryStatus
from models.chat import ChatRequest

from database.database import SessionLocal
from database.repository_metadata import save_metadata

from services.parser import count_files
from services.git_service import clone_repository
from services.repository_metadata_service import get_repository_metadata
from services.indexing_service import index_repository
from services.chat_service import answer_question
from services.guide_generator import generate_guide
from services.knowledge_graph import build_knowledge_graph
from models.chat_history_db import ChatHistoryDB





router = APIRouter()


@router.get("/analyze-repository")
def analyze_repository():

    repo_path = "test_repo"

    file_counts = count_files(repo_path)

    metadata = get_repository_metadata(repo_path)

    return {
        "python_files": file_counts["python_files"],
        "javascript_files": file_counts["javascript_files"],
        "java_files": file_counts["java_files"],
        "metadata": metadata
    }


@router.post("/upload-repository")
def upload_repository(repo: RepositoryRequest):

    db = SessionLocal()

    try:

        repository = RepositoryDB(
            repo_url=repo.repo_url,
            status=RepositoryStatus.PENDING
        )

        db.add(repository)
        db.commit()
        db.refresh(repository)

        repository.status = RepositoryStatus.CLONING
        db.commit()

        print("Cloning repository...")

        repo_path = clone_repository(
            repo.repo_url,
            repository.id
        )

        print("Extracting metadata...")

        metadata = get_repository_metadata(
            repo_path
        )

        print("Saving metadata...")

        save_metadata(
            repository.id,
            metadata
        )

        print("Starting indexing...")

        index_repository(
            repository.id,
            metadata
        )

        print("Indexing completed")

        repository.status = RepositoryStatus.READY
        db.commit()

        return {
            "repo_id": repository.id,
            "status": repository.status
        }

    except Exception as e:

        print("ERROR:", str(e))

        try:
            repository.status = RepositoryStatus.FAILED
            db.commit()
        except:
            pass

        return {
            "error": str(e)
        }

    finally:
        db.close()


@router.get("/repository/{repo_id}/status")
def get_repository_status(repo_id: int):

    db = SessionLocal()

    try:

        repository = (
            db.query(RepositoryDB)
            .filter(RepositoryDB.id == repo_id)
            .first()
        )

        if repository is None:
            return {
                "error": "Repository not found"
            }

        return {
            "repo_id": repository.id,
            "status": repository.status
        }

    finally:
        db.close()


@router.post("/chat")
def chat(request: ChatRequest):

    db = SessionLocal()

    try:

        result = answer_question(
            repo_id=request.repo_id,
            question=request.question
        )

        history = ChatHistoryDB(
            repo_id=request.repo_id,
            question=request.question,
            answer=result.get("answer", "")
        )

        db.add(history)
        db.commit()

        return result

    except Exception as e:

        db.rollback()

        return {
            "error": str(e)
        }

    finally:

        db.close()

@router.post("/generate-guide")
def generate_repository_guide(repo_id: int):

    repo_path = f"repos/repo_{repo_id}"

    guide = generate_guide(repo_path)

    return {
        "guide": guide
    }
@router.post("/knowledge-graph")
def knowledge_graph(repo_id: int):

    repo_path = f"repos/repo_{repo_id}"

    graph = build_knowledge_graph(
        repo_path
    )

    return graph