import redis
import json


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


# ==========================
# Metadata Cache
# ==========================

def cache_metadata(
    repo_id,
    metadata
):

    redis_client.set(
        f"metadata:{repo_id}",
        json.dumps(metadata)
    )


def get_metadata(
    repo_id
):

    data = redis_client.get(
        f"metadata:{repo_id}"
    )

    if data:
        return json.loads(data)

    return None


# ==========================
# Search Cache
# ==========================

def cache_search(
    query,
    results
):

    redis_client.set(
        f"search:{query}",
        json.dumps(results)
    )


def get_search(
    query
):

    data = redis_client.get(
        f"search:{query}"
    )

    if data:
        return json.loads(data)

    return None


# ==========================
# Embedding Cache
# ==========================

def cache_embedding(
    text,
    embedding
):

    redis_client.set(
        f"embedding:{text}",
        json.dumps(embedding)
    )


def get_embedding(
    text
):

    data = redis_client.get(
        f"embedding:{text}"
    )

    if data:
        return json.loads(data)

    return None