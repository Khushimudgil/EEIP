# test_repo_chunks.py

from services.parser import get_python_files
from services.python_ast_parser import parse_python_file

files = get_python_files("repos/fastapi")

total_chunks = 0

for file in files[:5]:

    parsed = parse_python_file(file)

    total_chunks += len(parsed["chunks"])

    print(file)
    print("chunks:", len(parsed["chunks"]))
    print("-" * 50)

print("TOTAL CHUNKS:", total_chunks)