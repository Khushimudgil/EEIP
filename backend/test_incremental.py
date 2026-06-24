from services.incremental_service import (
    get_changed_files
)

print(
    get_changed_files(
        "test_repo"
    )
)
