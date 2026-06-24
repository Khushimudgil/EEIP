import ast
import os


def parse_python_file(file_path):

    metadata = {
        "file": os.path.basename(file_path),
        "language": "python",
        "imports": [],
        "chunks": []
    }

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            source_code = file.read()

        lines = source_code.splitlines()

        tree = ast.parse(source_code)

        # =====================
        # IMPORTS
        # =====================

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for alias in node.names:
                    metadata["imports"].append(
                        alias.name
                    )

            elif isinstance(
                node,
                ast.ImportFrom
            ):

                if node.module:
                    metadata["imports"].append(
                        node.module
                    )

        # =====================
        # CLASSES + FUNCTIONS
        # =====================

        for node in tree.body:

            # =====================
            # CLASS
            # =====================

            if isinstance(
                node,
                ast.ClassDef
            ):

                class_code = "\n".join(
                    lines[
                        node.lineno - 1:
                        node.end_lineno
                    ]
                )

                metadata["chunks"].append({

                    "type": "class",
                    "name": node.name,

                    "file": metadata["file"],
                    "file_path": file_path,

                    "language": "python",

                    "class_name": node.name,
                    "function_name": None,

                    "start_line": node.lineno,
                    "end_line": node.end_lineno,

                    "code": class_code
                })

                # =====================
                # METHODS
                # =====================

                for child in node.body:

                    if isinstance(
                        child,
                        (
                            ast.FunctionDef,
                            ast.AsyncFunctionDef
                        )
                    ):

                        method_code = "\n".join(
                            lines[
                                child.lineno - 1:
                                child.end_lineno
                            ]
                        )

                        metadata["chunks"].append({

                            "type": "method",
                            "name": child.name,

                            "file": metadata["file"],
                            "file_path": file_path,

                            "language": "python",

                            "class_name": node.name,
                            "function_name": child.name,

                            "start_line": child.lineno,
                            "end_line": child.end_lineno,

                            "code": method_code
                        })

            # =====================
            # TOP LEVEL FUNCTION
            # =====================

            elif isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef
                )
            ):

                function_code = "\n".join(
                    lines[
                        node.lineno - 1:
                        node.end_lineno
                    ]
                )

                metadata["chunks"].append({

                    "type": "function",
                    "name": node.name,

                    "file": metadata["file"],
                    "file_path": file_path,

                    "language": "python",

                    "class_name": None,
                    "function_name": node.name,

                    "start_line": node.lineno,
                    "end_line": node.end_lineno,

                    "code": function_code
                })

        return metadata

    except SyntaxError as e:

        return {
            "file": os.path.basename(file_path),
            "error": f"Invalid Python syntax: {str(e)}"
        }

    except Exception as e:

        return {
            "file": os.path.basename(file_path),
            "error": str(e)
        }