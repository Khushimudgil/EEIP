from services.repository_dedup_service import (
    repository_exists,
    save_repository
)

repo_url = (
    "https://github.com/fastapi/fastapi"
)

commit_sha = "abc123"

print(
    repository_exists(
        repo_url,
        commit_sha
    )
)

save_repository(
    repo_url,
    commit_sha
)

print(
    repository_exists(
        repo_url,
        commit_sha
    )
)