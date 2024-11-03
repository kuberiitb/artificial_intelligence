
Tools are ways to call external functions 
```
from openai import OpenAI
client = OpenAI(api_key="ENTER YOUR KEY HERE")
response= client.chat.completions.create(
  model="gpt-4o-mini",
  messages=messages,
  tools=function_definition,
)
```
