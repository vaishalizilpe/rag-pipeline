# What Is LangChain

## 1. The problem it solves
Talking to an LLM directly (raw API call) means writing a lot of repetitive plumbing yourself: formatting prompts, parsing responses, connecting to a vector database, chaining multiple steps together. LangChain is a Python library that gives you pre-built pieces for all of that.

## 2. Think of it as Lego blocks for LLM apps
Each block does one job:
- A **model** block talks to an LLM (Claude, GPT, etc.)
- An **embedding** block turns text into vectors (numbers that capture meaning)
- A **vector store** block saves and searches those vectors
- A **retriever** block fetches relevant chunks for a question
- A **prompt template** block formats your question + retrieved context before sending it to the model

## 3. You snap the blocks together into a "chain"
For RAG specifically, the chain is:
question → retriever finds relevant chunks → prompt template combines question + chunks → model generates an answer.
That whole sequence is what Day 6 of the training plan builds.

## 4. Why it matters
Without LangChain, you'd hand-write the code to call Claude's API, hand-write cosine similarity search, hand-write prompt formatting. LangChain gives you tested, standard versions of all of that, so you spend your time on the RAG logic, not boilerplate. It's also the library most job postings and interviews reference by name.

## 5. What's installed for this course, and why
| Package | Purpose |
|---|---|
| `langchain` | Core chain-building logic |
| `langchain-community` | Community-contributed integrations (vector stores, loaders) |
| `langchain-anthropic` | Lets LangChain talk to Claude specifically |
| `chromadb` | Vector store — where embedded chunks live |
| `sentence-transformers` | Generates embeddings locally, free, no API key |

Note: Anthropic doesn't offer an embeddings API. Claude handles generation; `sentence-transformers` handles embeddings, running locally at no cost.
