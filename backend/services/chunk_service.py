def extract_chunks(metadata):

    chunks = []

    for file_data in metadata:

        if "chunks" not in file_data:
            continue

        for chunk in file_data["chunks"]:

            chunks.append({
                "file": file_data["file"],
                "language": file_data["language"],
                "chunk_name": chunk.get("chunk_name"),
                "chunk_type": chunk.get("chunk_type"),
                "code": chunk.get("code")
            })

    return chunks