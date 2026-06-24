import re

def classify_query(query: str):

    query = query.lower().strip()

    if re.search(r"\w+\(\)", query):
        return "CODE"

    search_keywords = [
        "where",
        "find",
        "which file",
        "location",
        "located",
        "search"
    ]

    code_keywords = [
        "function",
        "method",
        "class",
        "code",
        "implementation",
        "source code",
        "walk through",
        "explain"
    ]

    summary_keywords = [
        "what does",
        "summary",
        "overview",
        "architecture",
        "purpose",
        "describe"
    ]

    # SEARCH FIRST
    for keyword in search_keywords:
        if keyword in query:
            return "SEARCH"

    # CODE SECOND
    for keyword in code_keywords:
        if keyword in query:
            return "CODE"

    # SUMMARY THIRD
    for keyword in summary_keywords:
        if keyword in query:
            return "SUMMARY"

    return "SEARCH"