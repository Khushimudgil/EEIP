from services.repository_metadata_service import get_repository_metadata

result = get_repository_metadata("test_files")

print(result)