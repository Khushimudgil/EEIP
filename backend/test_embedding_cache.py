from services.redis_service import (
    cache_embedding,
    get_embedding
)


embedding = [
    0.1,
    0.2,
    0.3,
    0.4
]


cache_embedding(
    "authenticate user",
    embedding
)

print(
    get_embedding(
        "authenticate user"
    )
)