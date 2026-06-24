from services.change_detector import (
    file_changed
)

file_path = "test_repo/main.py"

print(
    file_changed(file_path)
)

print(
    file_changed(file_path)
)