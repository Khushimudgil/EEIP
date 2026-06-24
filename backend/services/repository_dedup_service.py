from services.repository_hash_service import (
    generate_repository_hash
)

processed_repositories = {}


def repository_exists(
    repo_url,
    commit_sha
):

    repo_hash = generate_repository_hash(
        repo_url,
        commit_sha
    )

    return repo_hash in processed_repositories


def save_repository(
    repo_url,
    commit_sha
):

    repo_hash = generate_repository_hash(
        repo_url,
        commit_sha
    )

    processed_repositories[
        repo_hash
    ] = True