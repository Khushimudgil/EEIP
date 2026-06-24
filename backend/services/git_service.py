import git
import os


def clone_repository(repo_url, repo_id):

    repo_path = f"repos/repo_{repo_id}"

    if os.path.exists(repo_path):
        return repo_path

    git.Repo.clone_from(
        repo_url,
        repo_path
    )

    return repo_path