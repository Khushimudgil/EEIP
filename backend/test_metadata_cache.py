from services.redis_service import (
    cache_metadata,
    get_metadata
)

sample = {
    "repo": "fastapi",
    "files": 100
}

cache_metadata(
    1,
    sample
)

print(
    get_metadata(1)
)