import os

from services.change_detector import (
    file_changed
)


def get_changed_files(repo_path):

    changed_files = []

    for root, dirs, files in os.walk(
        repo_path
    ):

        for file in files:

            if not file.endswith(
                (
                    ".py",
                    ".js",
                    ".java"
                )
            ):
                continue

            file_path = os.path.join(
                root,
                file
            )

            if file_changed(
                file_path
            ):

                changed_files.append(
                    file_path
                )

    return changed_files