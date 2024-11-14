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
