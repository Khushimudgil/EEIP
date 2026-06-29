from services.repository_metadata_service import get_repository_metadata


def generate_guide(repo_path):

    metadata = get_repository_metadata(repo_path)

    total_files = len(metadata)

    languages = set()
    important_files = []

    total_classes = 0
    total_functions = 0
    total_methods = 0

    for file_data in metadata:

        language = file_data.get("language")
        if language:
            languages.add(language)

        filename = file_data.get("file")
        if filename:
            important_files.append(filename)

        for chunk in file_data.get("chunks", []):

            chunk_type = chunk.get("type", "").lower()

            if chunk_type == "class":
                total_classes += 1

            elif chunk_type == "function":
                total_functions += 1

            elif chunk_type == "method":
                total_methods += 1

    guide = f"""
# Project Overview

This repository contains {total_files} source files.

Languages Used:
{", ".join(sorted(languages))}

Total Classes: {total_classes}

Total Functions: {total_functions}

Total Methods: {total_methods}

# Architecture

GitHub Repository
        ↓
Repository Parser
        ↓
Metadata Extraction
        ↓
Embedding Generation
        ↓
Qdrant Vector Database
        ↓
Dense Vector Search
        ↓
BM25 Search
        ↓
Hybrid Retrieval
        ↓
Reciprocal Rank Fusion (RRF)
        ↓
Cross Encoder Reranking
        ↓
Gemini LLM
        ↓
Answer Generation

# Entry Points

main.py
api/repository.py

# Folder Structure

api/
services/
models/
database/
repos/

# Important Files

"""

    for file in important_files[:10]:
        guide += f"- {file}\n"

    guide += """

# Features

• Repository Upload
• Metadata Extraction
• Code Chunking
• Embedding Generation
• Vector Search
• BM25 Search
• Hybrid Retrieval
• RRF Fusion
• Cross Encoder Reranking
• AI Repository Chat
• Multi-Agent Routing
• Source Citations
• Repository Guide Generator

# How To Run

1. Install Dependencies

pip install -r requirements.txt

2. Start Backend

python -m uvicorn main:app --reload --port 8001

3. Start Frontend

npm install
npm run dev

4. Open Application

http://localhost:5173

# Developer Notes

• Repository metadata is generated using AST parsing.
• Embeddings are stored in Qdrant.
• BM25 provides keyword-based retrieval.
• Dense retrieval uses sentence embeddings.
• Hybrid retrieval combines dense search and BM25.
• Results are merged using Reciprocal Rank Fusion (RRF).
• Cross Encoder reranks the retrieved chunks.
• Gemini generates repository-aware answers with citations.

Generated automatically by EEIP.
"""

    return guide