from services.status_service import (
    get_repository_status
)

status = get_repository_status(
    1
)

print(status)