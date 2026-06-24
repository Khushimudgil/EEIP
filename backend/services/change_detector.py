from services.file_hash_service import get_file_hash

file_hashes = {}


def file_changed(file_path):

    current_hash = get_file_hash(
        file_path
    )

    old_hash = file_hashes.get(
        file_path
    )

    if old_hash != current_hash:

        file_hashes[file_path] = (
            current_hash
        )

        return True

    return False