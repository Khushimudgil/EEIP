import os


def generate_repository_summary(repo_path):

    summary = {
        "repository_name": os.path.basename(repo_path),
        "python_files": 0,
        "javascript_files": 0,
        "java_files": 0,
        "modules": [],
        "entry_points": []
    }

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".py"):
                summary["python_files"] += 1

            elif file.endswith(".js"):
                summary["javascript_files"] += 1

            elif file.endswith(".java"):
                summary["java_files"] += 1

    for item in os.listdir(repo_path):

        path = os.path.join(repo_path, item)

        if os.path.isdir(path):

            summary["modules"].append(item)

    entry_candidates = [
        "main.py",
        "app.py",
        "server.py",
        "run.py"
    ]

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file in entry_candidates:

                summary["entry_points"].append(file)

    return summary
def format_repository_summary(summary):

    text = f"""
Repository Overview
-------------------

Repository Name:
{summary['repository_name']}


Languages
---------

Python Files: {summary['python_files']}
JavaScript Files: {summary['javascript_files']}
Java Files: {summary['java_files']}


Main Modules
------------

{', '.join(summary['modules']) if summary['modules'] else 'No modules detected'}


Entry Points
------------

{', '.join(summary['entry_points']) if summary['entry_points'] else 'No entry points detected'}
"""

    return text