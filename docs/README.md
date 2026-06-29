# 🚀 EEIP - Enterprise Engineering Intelligence Platform

AI-powered Repository Intelligence Platform that understands GitHub repositories using Large Language Models (LLMs), Hybrid Search, and Vector Databases.

---

## 📖 Overview

EEIP helps developers understand unfamiliar codebases by automatically analyzing GitHub repositories and providing AI-powered insights.

Instead of manually browsing hundreds of source files, users can upload a repository and instantly:

- Analyze repository structure
- Search code semantically
- Ask natural language questions
- Generate repository documentation
- Explore repository knowledge graphs

---

## ✨ Features

### 📂 Repository Upload
- Upload any public GitHub repository
- Automatic repository cloning
- Repository indexing

### 🧠 AI Repository Chat
- Ask questions in natural language
- AI understands project context
- Source-aware responses
- Repository-specific answers

### 🔍 Hybrid Search
- Dense Vector Search
- BM25 Keyword Search
- Reciprocal Rank Fusion (RRF)
- Gemini-powered responses

### 📚 Repository Guide Generator
Automatically generates:
- Project overview
- Folder structure
- Technologies used
- Main classes
- Main functions

### 🕸 Knowledge Graph
Visual repository summary including:
- Files
- Classes
- Functions
- Methods
- Imports

### 📊 Dashboard
- Repository statistics
- Total repositories
- Files parsed
- Embeddings stored
- AI queries

---

# 🏗 Architecture

```
GitHub Repository
        │
        ▼
Repository Cloning
        │
        ▼
Metadata Extraction
        │
        ▼
Language Parsers
(Python • Java • JavaScript)
        │
        ▼
Chunk Generation
        │
        ▼
Embedding Generation
        │
        ▼
Qdrant Vector Database
        │
        ▼
Hybrid Retrieval
(Dense + BM25 + RRF)
        │
        ▼
Gemini LLM
        │
        ▼
Repository Chat
```

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- Qdrant Vector Database
- Google Gemini API
- GitPython
- Redis (optional)

## Frontend

- React
- Vite
- Tailwind CSS
- Axios
- Lucide React

## AI / ML

- Sentence Transformers
- Dense Embeddings
- BM25
- Hybrid Retrieval
- Reciprocal Rank Fusion (RRF)

---

# 📁 Project Structure

```
EEIP
│
├── backend
│   ├── api
│   ├── services
│   ├── models
│   ├── database
│   ├── rag
│   └── repos
│
├── frontend
│   ├── src
│   ├── components
│   ├── pages
│   └── services
│
└── docs
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Khushimudgil/EEIP.git
```

---

## Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run backend

```bash
uvicorn main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🌐 API Endpoints

## Repository

```
POST /upload-repository
```

Uploads and indexes a GitHub repository.

---

## Status

```
GET /repository/{repo_id}/status
```

Returns indexing status.

---

## Chat

```
POST /chat
```

Ask questions about a repository.

---

## Guide

```
POST /generate-guide
```

Generate project documentation.

---

## Knowledge Graph

```
POST /knowledge-graph
```

Generate repository graph.

---

## Dashboard

```
GET /dashboard-stats
```

Returns project statistics.

---

# 💡 Example Workflow

1. Upload GitHub Repository

↓

2. Repository Cloning

↓

3. Metadata Extraction

↓

4. Embedding Generation

↓

5. Vector Storage (Qdrant)

↓

6. Hybrid Retrieval

↓

7. Ask AI Questions

↓

8. Receive Source-aware Answers

---

# 🎯 Future Improvements

- Authentication
- Private repository support
- Interactive Knowledge Graph
- Multi-language support
- Repository comparison
- Docker deployment
- Kubernetes deployment

---

# 👩‍💻 Author

**Khushi Mudgil**

B.Tech Electronics and Communication Engineering

Netaji Subhas University of Technology (NSUT)

---

