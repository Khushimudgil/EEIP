import re
import os




def parse_java_file(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("CONTENT START")
        print(repr(content))
        print("CONTENT END")

    print(content)

    classes = re.findall(
        r'class\s+([A-Za-z_][A-Za-z0-9_]*)',
        content
    )

    methods = re.findall(
        r'(?:public|private|protected)?\s*(?:static\s+)?(?:\w+)\s+(\w+)\s*\(',
        content
    )

    imports = re.findall(
        r'import\s+([\w\.]+);',
        content
    )

    print("CLASSES:", classes)
    print("METHODS:", methods)
    print("IMPORTS:", imports)

    return {
        "file": os.path.basename(file_path),
        "language": "java",
        "classes": classes,
        "functions": [],
        "methods": methods,
        "imports": imports
    }