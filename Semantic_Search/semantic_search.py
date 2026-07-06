from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "LangChain helps build AI agents.",
    "Python is a programming language.",
    "Bananas are rich in potassium.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks.",
    "The capital of France is Paris."
]

query = "How can I build an AI assistant?"

# Generate embeddings
doc_embeddings = model.encode(documents)
query_embedding = model.encode(query)

# Calculate similarity
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Pair document with score
results = list(zip(documents, scores))

# Sort by score
results.sort(key=lambda x: x[1], reverse=True)

# Retrieve Top 3
top_k = 3

print("\nTop Results:\n")

for doc, score in results[:top_k]:
    print(f"{score:.3f} --> {doc}")