from rank_bm25 import BM25Okapi

bm25 = None
documents = []


def build_bm25_index(chunks):

    global bm25
    global documents

    documents = chunks

    tokenized_docs = []

    for chunk in chunks:

        if "code" not in chunk:
            continue

        tokenized_docs.append(
            chunk["code"].split()
        )

    bm25 = BM25Okapi(
        tokenized_docs
    )

    print("BM25 Index Built")


def search_bm25(
    query,
    top_k=5
):

    global bm25
    global documents

    if bm25 is None:
        print("BM25 not available")
        return []

    query_tokens = query.split()

    scores = bm25.get_scores(
        query_tokens
    )

    ranked = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_k]