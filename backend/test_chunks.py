from services.python_ast_parser import parse_python_file

data = parse_python_file(
    "repos/fastapi/docs_src/async_tests/app_a_py310/test_main.py"
)

import json

print(json.dumps(data, indent=4))
print("\nTOTAL CHUNKS:", len(data["chunks"]))

for chunk in data["chunks"]:
    print("\n----------------")
    print("TYPE:", chunk["type"])
    print("NAME:", chunk["name"])