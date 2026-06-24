import hashlib


def generate_repository_hash(
    repo_url,
    commit_sha
):

    value = (
        repo_url +
        commit_sha
    )

    return hashlib.md5(
        value.encode()
    ).hexdigest()