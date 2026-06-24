# test_repository_task.py

from tasks import process_repository

result = process_repository.delay(
    "https://github.com/fastapi/fastapi"
)

print(
    result.id
)