import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Documents
documents = [
    "LangChain helps build AI agents.",
    "Python is a programming language.",
    "Bananas are rich in potassium.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks.",
    "The capital of France is Paris."
]

# Create embeddings
embeddings = model.encode(documents)
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(embeddings)

# Query
query = "How can I build an AI assistant?"

query_embedding = model.encode([query])
query_embedding = np.array(query_embedding).astype("float32")

# Search
k = 3
distances, indices = index.search(query_embedding, k)

print("\nTop Results:\n")

for i, idx in enumerate(indices[0]):
    print(f"Rank {i+1}")
    print(f"Document : {documents[idx]}")
    print(f"Distance : {distances[0][i]:.4f}")
    print("-" * 40)