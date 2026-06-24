from services.redis_service import (
    cache_search,
    get_search
)

results = [
    {
        "file": "auth.py",
        "chunk": "authenticate_user"
    }
]

cache_search(
    "authentication",
    results
)

print(
    get_search("authentication")
)