# 🧠 CiviLens Backend

---

## 🚀 Overview

The backend is responsible for:

* Building and maintaining a **graph-based knowledge store** of events and entities.
* Handling **retrieval pipelines** that combine semantic and relational search.
* Managing **LLM augmentations** to produce context-aware responses.
* Serving API endpoints for frontend tools like **OpenUI** or dashboards.

---

## 🏗️ Project Structure

```
civilens-backend/
├── src/
│   ├── api/                # FastAPI routes (query, ingest, generate)
│   ├── core/               # Configs, logging, dependency injection
│   ├── rag/
│   │   ├── retriever/      # Graph + vector search logic
│   │   ├── generator/      # LLM response generation
│   │   └── pipeline/       # Retrieval-Augmented Generation flow
│   ├── graph/
│   │   ├── builder.py      # Builds/updates the knowledge graph
│   │   └── schema.py       # Entity & relation definitions
│   ├── db/
│   │   └── models.py       # SQLServer / ORM models
│   ├── embeddings/
│   │   └── embedder.py     # SentenceTransformers or OpenAI embeddings
│   ├── tests/
│   └── main.py             # App entry point
├── requirements.txt
├── .env.example
├── Dockerfile
└── README.md
```

---

## 🧰 Tech Stack

| Component            | Technology                               |
| -------------------- | ---------------------------------------- |
| **Language**         | Python 3.11+                             |
| **Framework**        | FastAPI                                  |
| **Graph DB**         | Neo4j / ArangoDB                         |
| **Vector Store**     | FAISS / Qdrant                           |
| **LLM Integration**  | OpenAI API / Ollama                      |
| **Embedding Model**  | SentenceTransformers / OpenAI Embeddings |
| **Orchestration**    | LangChain / LlamaIndex                   |
| **Containerization** | Docker                                   |
| **Testing**          | Pytest                                   |

---


## 🧭 Roadmap

* [ ] Implement graph-based retrieval
* [ ] Integrate vector search
* [ ] Add LLM response generation
* [ ] Deploy via Docker & CI/CD

---

## 🧩 References

* [XGraphRAG: Interactive Visual Analysis for Graph-based RAG](https://arxiv.org/abs/2406.09388)
* [LangChain Documentation](https://python.langchain.com)
* [Neo4j Graph Data Science](https://neo4j.com/developer/graph-data-science/)
