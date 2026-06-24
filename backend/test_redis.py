from services.redis_service import redis_client

redis_client.set(
    "name",
    "PHIVO"
)

value = redis_client.get(
    "name"
)

print(value)