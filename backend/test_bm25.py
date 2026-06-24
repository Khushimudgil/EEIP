from services.bm25_service import (
    build_bm25_index,
    search_bm25
)

chunks = [
    {
        "name": "login",
        "type": "function",
        "code": "user login authentication password"
    },
    {
        "name": "register",
        "type": "function",
        "code": "user register create account"
    }
]

build_bm25_index(chunks)

results = search_bm25(
    "authentication login"
)

print(results)