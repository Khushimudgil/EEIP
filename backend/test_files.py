# test_files.py

from services.parser import get_python_files

files = get_python_files("repos/fastapi")

print("TOTAL FILES:", len(files))

for file in files[:10]:
    print(file)