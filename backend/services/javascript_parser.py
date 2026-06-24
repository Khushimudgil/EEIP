import re
import os


def parse_javascript_file(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    classes = re.findall(
        r'class\s+([A-Za-z_][A-Za-z0-9_]*)',
        content
    )

    functions = re.findall(
        r'function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(',
        content
    )

    imports = re.findall(
        r'import\s+.*?from\s+[\'"]([^\'"]+)[\'"]',
        content
    )

    chunks = []

    for function_name in functions:

        chunks.append(
            {
                "type": "function",
                "name": function_name,
                "file": os.path.basename(file_path),
                "file_path": file_path,
                "language": "javascript",
                "class_name": None,
                "function_name": function_name,
                "code": content
            }
        )

    return {
        "file": os.path.basename(file_path),
        "language": "javascript",
        "classes": classes,
        "functions": functions,
        "methods": [],
        "imports": imports,
        "chunks": chunks
    }