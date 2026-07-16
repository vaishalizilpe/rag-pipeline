# RAG Cheat Sheet
10-Day Plan | 1 hr/day | Goal: Job-ready

---

## Progress Tracker
```
[ ] Day 1  ░░░░░░░░░░  What RAG Solves
[ ] Day 2  ░░░░░░░░░░  Embeddings and Similarity
[ ] Day 3  ░░░░░░░░░░  Chunking Strategy
[ ] Day 4  ░░░░░░░░░░  Vector Stores and Indexing
[ ] Day 5  ░░░░░░░░░░  Retrieval
[ ] Day 6  ░░░░░░░░░░  Full Pipeline (Retrieve + Generate)
[ ] Day 7  ░░░░░░░░░░  Query Transformation
[ ] Day 8  ░░░░░░░░░░  Hybrid Search and Reranking
[ ] Day 9  ░░░░░░░░░░  Evaluation with RAGAS
[ ] Day 10 ░░░░░░░░░░  Capstone
```
Fill a bar as you complete each day: ░ = todo █ = done

---

## Concept Map (simplified)
```
Embeddings ──► Chunking ──► Vector Stores ──► Retrieval
                                                   │
Query Transformation ──► Hybrid Search & Reranking ┘
                                                   │
                                    Evaluation (RAGAS) ──► Capstone
```

---

## Learning Arc
Day 1: What RAG Solves → Day 2: Embeddings and Similarity → Day 3: Chunking Strategy → Day 4: Vector Stores and Indexing → Day 5: Retrieval → Day 6: Full Pipeline → Day 7: Query Transformation → Day 8: Hybrid Search and Reranking → Day 9: Evaluation → Day 10: Capstone

---

## Key Insights (one per day)
- Day 1: RAG doesn't make the model smarter, it hands the model a fresh, attributable source of truth.
- Day 2: An embedding is a coordinate, not a summary, closeness comes from context not shared words.
- Day 3: Chunk size is a precision/recall tradeoff, not a technical detail.
- Day 4: A vector store is an approximate nearest-neighbor index, not a text database.
- Day 5: Debugging a bad answer starts with what retrieval returned, not the prompt.
- Day 6: The prompt must force the model to answer only from context, or it blends in its own memory.
- Day 7: The user's raw question is often a bad search query, transform it before embedding.
- Day 8: Vector search misses exact terms, hybrid search and reranking fix different failure modes.
- Day 9: "It looks right" is not evaluation, faithfulness and context precision are separately measurable.
- Day 10: PhD level means you can justify every design decision under pushback.

---

## Anchor Resources
1. LangChain RAG Tutorial — https://python.langchain.com/docs/tutorials/rag/
2. freeCodeCamp RAG From Scratch — https://www.freecodecamp.org/news/mastering-rag-from-scratch/
3. Pinecone Learn RAG Series — https://www.pinecone.io/learn/series/rag/
4. DeepLearning.AI RAG Course — https://www.deeplearning.ai/courses/retrieval-augmented-generation
5. RAGAS Docs — https://docs.ragas.io/

---

## Daily Checklist
- [ ] Day 1: Set up environment, capture an LLM hallucination — https://www.pinecone.io/learn/series/rag/
- [ ] Day 2: Embed and rank sentences by cosine similarity — https://python.langchain.com/docs/concepts/embedding_models/
- [ ] Day 3: Chunk a real document 3 ways, compare — https://python.langchain.com/docs/concepts/text_splitters/
- [ ] Day 4: Build a persisted Chroma index — https://python.langchain.com/docs/concepts/vectorstores/
- [ ] Day 5: Wrap index in a retriever, judge precision manually — https://python.langchain.com/docs/concepts/retrievers/
- [ ] Day 6: Wire retriever to generation with grounding + refusal — https://python.langchain.com/docs/tutorials/rag/
- [ ] Day 7: Add multi-query retrieval, compare before/after — https://python.langchain.com/docs/how_to/MultiQueryRetriever/
- [ ] Day 8: Add hybrid search (BM25 + vector) or reranking — https://python.langchain.com/docs/how_to/ensemble_retriever/
- [ ] Day 9: Run RAGAS on a 5-question eval set — https://docs.ragas.io/en/stable/getstarted/
- [ ] Day 10: Build and defend the capstone RAG system

---

## Common Traps (quick reminders)
1. Untested chunking: validate chunk size against real queries, don't just guess.
2. Trusting fluent answers: always inspect retrieved chunks, not just the final answer.
3. No "don't know" instruction: explicitly forbid the model from using outside knowledge.
4. Vector-only search on exact terms: add BM25/hybrid search for codes, names, acronyms.
5. Skipping evaluation: build a small RAGAS eval set early, rerun after every change.

---

## Capstone Project
Grounded Q&A System Over a Real Multi-Document Corpus — hybrid retrieval, grounded generation with citations, explicit refusal, RAGAS-scored.

---

## Confidence Test
Build a chunked, hybrid-search, cited, refusal-capable RAG system from scratch on a new document set in under 90 minutes, with RAGAS scores reported.
Pass if: grounded + correct refusal without notes / can explain chunking and retrieval choices verbally / faithfulness score reported and explained.

---

## PhD Depth (after you finish)
1. freeCodeCamp advanced segments (RAPTOR, ColBERT, CRAG) — https://www.freecodecamp.org/news/mastering-rag-from-scratch/
2. DeepLearning.AI Agentic RAG with LlamaIndex — https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/
