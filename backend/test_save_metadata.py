from models.repository_db import RepositoryDB
from database.repository_metadata import save_metadata

sample_metadata = [
    {
        "file": "UserService.java",
        "language": "java",
        "classes": ["UserService"],
        "functions": [],
        "methods": ["login", "logout"],
        "imports": ["java.util.List"]
    }
]

save_metadata(3, sample_metadata)

print("Saved Successfully")