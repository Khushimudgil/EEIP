from services.repository_metadata_service import get_repository_metadata

metadata = get_repository_metadata(
    "repos/fastapi"
)

print(type(metadata))
print(len(metadata))
print(metadata[0])