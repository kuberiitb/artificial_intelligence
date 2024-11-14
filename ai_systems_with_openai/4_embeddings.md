## The embeddings endpoint
Embedding is a method to represent the data in a vector of continuous numbers. We can provide these vectors to machine learning algorithms and models. Similar texts will have the same embedding vectors, and two different texts will have very different embeddings.

### Python code to get embedding
```
from openai import OpenAI
client = OpenAI(api_key="XYZ")

response = client.embeddings.create(
    input="The burger was fantastic.",
    model="text-embedding-ada-002"
)

print(response.data[0].embedding)
print(len(response.data[0].embedding))
```

### Cosine similarity using embeddings

```
from openai import OpenAI
from scipy.spatial.distance import cosine

client = OpenAI(api_key="XYZ")

# Get embeddings for two statements
response = client.embeddings.create(
    input=["The burger was fantastic.", "I really enjoyed the burger."],
    model="text-embedding-ada-002"
)

# Extract embeddings
embedding1 = response.data[0].embedding
embedding2 = response.data[1].embedding

# Compute cosine similarity
similarity_score = 1 - cosine(embedding1, embedding2)
print("Cosine similarity between the two statements:", similarity_score)
```
