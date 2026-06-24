from pydantic import BaseModel

class RepositoryStatusUpdate(BaseModel):
    status: str