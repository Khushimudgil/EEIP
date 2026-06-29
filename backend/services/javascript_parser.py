import re
import os


def parse_javascript_file(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    lines = content.splitlines()

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

    # ----------------------------
    # Function Chunks
    # ----------------------------

    for function_name in functions:

        start_line = 1

        for index, line in enumerate(lines):

            if f"function {function_name}" in line:
                start_line = index + 1
                break

        chunks.append({

            "type": "function",
            "name": function_name,

            "file": os.path.basename(file_path),
            "file_path": file_path,

            "language": "javascript",

            "class_name": None,
            "function_name": function_name,

            "start_line": start_line,
            "end_line": len(lines),

            "code": content

        })

    # ----------------------------
    # Class Chunks
    # ----------------------------

    for class_name in classes:

        start_line = 1

        for index, line in enumerate(lines):

            if f"class {class_name}" in line:
                start_line = index + 1
                break

        chunks.append({

            "type": "class",
            "name": class_name,

            "file": os.path.basename(file_path),
            "file_path": file_path,

            "language": "javascript",

            "class_name": class_name,
            "function_name": None,

            "start_line": start_line,
            "end_line": len(lines),

            "code": content

        })

    return {

        "file": os.path.basename(file_path),

        "language": "javascript",

        "classes": classes,

        "functions": functions,

        "methods": [],

        "imports": imports,

        "chunks": chunks

    }