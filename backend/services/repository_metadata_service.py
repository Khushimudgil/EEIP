import os

from services.python_ast_parser import parse_python_file
from services.java_parser import parse_java_file
from services.javascript_parser import parse_javascript_file


def get_repository_metadata(repo_path):

    metadata = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            file_path = os.path.join(root, file)

            if file.endswith(".py"):

                metadata.append(
                    parse_python_file(file_path)
                )

            elif file.endswith(".java"):

                metadata.append(
                    parse_java_file(file_path)
                )

            elif file.endswith(".js"):

                metadata.append(
                    parse_javascript_file(file_path)
                )

    return metadata