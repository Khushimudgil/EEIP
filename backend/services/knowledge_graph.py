from services.repository_metadata_service import get_repository_metadata


def build_knowledge_graph(repo_path):

    metadata = get_repository_metadata(repo_path)

    files = []
    classes = []
    functions = []
    methods = []
    imports = set()

    for file_data in metadata:

        files.append(
            file_data.get("file")
        )

        for imp in file_data.get("imports", []):
            imports.add(imp)

        for chunk in file_data.get("chunks", []):

            chunk_type = chunk.get("type", "").lower()

            if chunk_type == "class":
                classes.append(
                    chunk.get("name")
                )

            elif chunk_type == "function":
                functions.append(
                    chunk.get("name")
                )

            elif chunk_type == "method":
                methods.append(
                    chunk.get("name")
                )

    return {
    "files": sorted(list(set(files))),
    "classes": sorted(list(set(classes))),
    "functions": sorted(list(set(functions))),
    "methods": sorted(list(set(methods))),
    "imports": sorted(list(imports))
    }