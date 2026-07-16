# Resume Tracking — RAG Pipeline Project

Purpose: don't let resume claims outrun what's actually built. Every bullet below is locked until its proof point exists in this repo.

---

## Current status (as of 2026-07-15)

- Repo: public on GitHub — https://github.com/vaishalizilpe/rag-pipeline
- Commits: 1 (curriculum + docs only)
- Code written: 0 days
- Proof points earned: 0

Plainly: right now this is a study plan, not a project. Nothing here supports a resume line yet. That's fine on Day 0, but the gap matters if you're job-hunting on a timeline — a resume bullet needs a working artifact behind it, not a folder of intentions.

---

## Proof ledger

Each skill you'd want to claim maps to a specific, checkable artifact. Don't add the skill to your resume until the artifact exists and works.

| Claim you'd want to make | Proof required | Status |
|---|---|---|
| "Built a RAG pipeline with LangChain" | `day6_full_rag_pipeline.py` runs end-to-end, retrieves + generates a grounded answer | Not started |
| "Implemented hybrid search (BM25 + vector)" | `day8_hybrid_and_rerank.py` with a documented before/after on a term-heavy query | Not started |
| "Evaluated RAG quality with RAGAS" | `day9_ragas_eval.py` with actual faithfulness/precision/recall numbers, not just "ran RAGAS" | Not started |
| "Shipped a production-style RAG system" | Capstone: multi-document corpus, hybrid retrieval, citations, explicit refusal on out-of-scope questions, RAGAS scores reported | Not started |

If you stop partway through the 10 days, your resume claim should stop at whatever day you actually finished, not "learned LangChain." Half a chunking exercise isn't a skill.

---

## Draft resume bullets (locked until earned)

**Minimum bar to write anything on a resume:** Day 6 complete (working retrieve-then-generate pipeline). Below that, this is a "currently building" line at most, not a bullet with a verb in past tense.

**If you stop at Day 6:**
> Built a retrieval-augmented generation pipeline (LangChain, Chroma, Claude) that grounds LLM answers in a private document corpus with source citation and explicit refusal on out-of-scope questions.

**If you finish through Day 9 (has numbers — this is the stronger version):**
> Built and evaluated a RAG pipeline (LangChain, Chroma, RAGAS) achieving [X]% faithfulness and [X]% context precision on a hand-written eval set; implemented hybrid BM25 + vector retrieval and query transformation to close identified retrieval gaps.

**If you finish the Day 10 capstone (strongest — this is the one worth leading with in interviews):**
> Designed and shipped a production-pattern RAG system over a multi-document corpus: hybrid retrieval, cross-encoder reranking, grounded generation with citations, and RAGAS-measured evaluation (faithfulness, context precision/recall) — [link to public repo].

Do not use the word "expert," "production-grade," or "scalable" unless you can defend it under a follow-up question in an interview. A 10-day self-study repo with one document is honest as "hands-on project," not as "production experience." Interviewers who work in this space will probe — the RAGAS numbers and your ability to explain chunking/retrieval tradeoffs out loud are what actually hold up, not the adjectives.

---

## What "linked to your resume" looks like when this is done

1. Repo stays public at the URL above — that's your evidence link.
2. README.md's capstone section becomes the project description you paraphrase in the bullet.
3. RAGAS scores go in the bullet as numbers, not "evaluated with RAGAS" — numbers are what differentiate you from someone who watched the same tutorials.
4. Update this file's "Current status" section after each day you complete, and move the matching row in the Proof ledger from "Not started" to "Done" with the commit hash.

---

## Next action

Zero days done, zero code. The fastest way to make this resume-relevant is Day 1 today — the environment setup + hallucination-capture script. Say the word and I'll scaffold `projects/day1/` and get you moving.
