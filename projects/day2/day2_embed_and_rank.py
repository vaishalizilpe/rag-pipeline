from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

query = "How do I reset my password?"

candidates = [
    "I forgot my login and can't get back into my account.",       # same meaning, no shared words
    "The bank approved my loan application yesterday.",             # unrelated, "bank" red herring
    "Click 'Forgot Password' on the sign-in page to get a reset link.",  # directly relevant
    "The river bank was flooded after the storm.",                  # unrelated, "bank" red herring
    "Password requirements: at least 8 characters, one number.",    # loosely related
]

query_vec = model.encode([query])
candidate_vecs = model.encode(candidates)

scores = cosine_similarity(query_vec, candidate_vecs)[0]
ranked = sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)

print(f"QUERY: {query}\n")
print("RANKED BY SIMILARITY:")
for i, (text, score) in enumerate(ranked, 1):
    print(f"{i}. [{score:.3f}] {text}")
