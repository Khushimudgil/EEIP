# test_celery.py

from tasks import add

result = add.delay(
    5,
    7
)

print(
    "Task ID:",
    result.id
)