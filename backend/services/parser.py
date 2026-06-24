import os
def get_python_files(repo_path):

    python_files = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".py"):

                python_files.append(
                    os.path.join(root, file)
                )

    return python_files

def count_files(repo_path):
    py_count = 0
    js_count = 0
    java_count = 0

    for root, dirs, files in os.walk(repo_path):
        for file in files:

            if file.endswith(".py"):
                py_count += 1

            elif file.endswith(".js"):
                js_count += 1

            elif file.endswith(".java"):
                java_count += 1

    return {
        "python_files": py_count,
        "javascript_files": js_count,
        "java_files": java_count
    }