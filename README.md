# 🧠 CiviLens  
### Graph-based Retrieval-Augmented Generation for Syrian Societal Events

> **Inspired by:** [*XGraphRAG: Interactive Visual Analysis for Graph-based Retrieval-Augmented Generation* (Ke Wang et al., 2024)](https://arxiv.org/abs/2406.06645)

---

## 🌍 Overview

**CiviLens** is a research-oriented project that explores **Graph-based Retrieval-Augmented Generation (GraphRAG)** applied to **Syrian societal events**.  
It leverages structured event data (similar to the Arabic ACLED dataset) and modern retrieval-generation techniques to answer complex, contextual questions about social and civic dynamics.

While traditional RAG systems enhance Large Language Models (LLMs) with retrieved textual data, CiviLens follows the **GraphRAG approach** from *XGraphRAG*, introducing a **knowledge graph** as an intermediate layer that captures relationships between events, actors, regions, and topics.

This graph structure helps:
- Improve contextual retrieval (via graph proximity and relationships)
- Enhance interpretability of retrieved information
- Provide structured, explainable answers about societal patterns

---

## 🎯 Project Goals

- 🧩 Build a **graph-augmented RAG pipeline** that integrates structured and unstructured data.
- 🧠 Support **context-aware QA** and analysis for event-based datasets.
- 📊 Explore the **interpretability and reasoning trace** of GraphRAG in a real-world domain.
- 🌐 Focus on **Syrian societal events**, using data similar to Arabic ACLED.

---

## ⚙️ System Overview

```

User Query
│
▼
Retriever ──► Graph-based Context Expansion ──► Generator (LLM)
│                                           │
▼                                           ▼
Event & Entity Graph (actors, regions)   Generated Answer + Evidence

```

**Main Components**
1. **Data Ingestion Layer** – Cleans and normalizes event data, builds the graph structure.  
2. **Retriever Layer** – Retrieves relevant nodes and edges using semantic + graph similarity.  
3. **Generator Layer** – Uses an LLM (Gemini 2.5 Flash) to produce contextual summaries.  
4. **Storage** – SQL Server for structured data, Qdrant for vectors, Neo4j for graph structure.  
5. **Frontend** – Simple React + OpenUI interface for query and visualization.  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| API Backend | FastAPI (Python) |
| Database | SQL Server |
| Vector Store | Qdrant / ChromaDB |
| Graph Storage | Neo4j / NetworkX |
| Embeddings | LaBSE / ArabicBERT |
| LLM | Gemini 2.5  |
| RAG Framework | LangChain / LlamaIndex |
| Frontend | React + OpenUI |
| Containerization | Docker Compose |

---

## 📁 Repository Structure

```

CiviLens/
│
├── backend/
│   ├── api/              # FastAPI endpoints
│   ├── core/             # RAG logic (retriever, generator, embeddings)
│   ├── data_ingestion/   # ETL scripts for event data
│   ├── db/               # DB and graph schema definitions
│   ├── config/           # Environment and logging
│   └── main.py           # Entry point
│
├── vector_store/
│   ├── init_vector_db.py
│   └── embed_documents.py
│
├── notebooks/           
│
├── frontend/             # UI for query interaction
│
├── docker-compose.yml
├── .env.example
├── README.md
└── requirements.txt

````

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/HasanKhadd0ur/CiviLens.git
cd CiviLens
````

### 2. Setup environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Start services

```bash
docker compose up
```

### 4. Run the API

```bash
uvicorn backend.main:app --reload
```

Then open: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Example Query

> “What were the major societal tensions in northern Syria during 2024?”

**CiviLens**:

* Retrieves related event clusters (conflicts, protests, civic actions)
* Expands context using graph relationships
* Generates a concise analytical answer with sources

---

## 🧠 Research Context

This project **does not reproduce** the full visualization framework from *XGraphRAG*,
but **adopts its conceptual methodology** — using a **graph-based retrieval layer** to enhance interpretability and contextual relevance in LLM-based QA systems.

---

## 📜 Citation

If you reference this project in your research, please cite the original XGraphRAG paper:

```
@article{wang2024xgraphrag,
  title={XGraphRAG: Interactive Visual Analysis for Graph-based Retrieval-Augmented Generation},
  author={Wang, Ke and Pan, Bo and Feng, Yingchaojie and Wu, Yuwei and Chen, Jieyi and Zhu, Minfeng and Chen, Wei},
  year={2024},
  journal={arXiv preprint arXiv:2406.06645}
}
```

---

## 🤝 Acknowledgments

CiviLens builds on the foundational ideas introduced in **XGraphRAG** and extends them to
the analysis of **Arabic and Syrian societal event data**, contributing toward transparent, explainable, and domain-specific RAG systems.

---