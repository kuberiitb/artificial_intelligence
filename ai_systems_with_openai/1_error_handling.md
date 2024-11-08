# Erros in openai API library -- 404 - model doesn't exists

# connection errors
- InternalServerError
- APIConnectionError
- APITimeoutError
Solution- Check connection config

# Reduce limitis error
- Conflict error
- RateLimitError
  - Too many requests -- use tenacity
  ```
  # Import the tenacity library
  from tenacity import retry, wait_random_exponential, stop_after_attempt
  
  client = OpenAI(api_key="<OPENAI_API_TOKEN>")
  
  # Add the appropriate parameters to the decorator
  @retry(wait=wait_random_exponential(min=5, max=40), stop=stop_after_attempt(4))
  def get_response(model, message):
      response = client.chat.completions.create(
        model=model,
        messages=[message]
      )
      return response.choices[0].message.content
  print(get_response("gpt-4o-mini", {"role": "user", "content": "List ten holiday destinations."}))
  ```

  - Too much text in the request -- use batching
  ```
  client = OpenAI(api_key="<OPENAI_API_TOKEN>")
  messages = []
  # Provide a system message and user messages to send the batch
  messages.append({
      "role": "system",
      "content": "convert given weights in kilometers to miles"})
  # Append measurements to the message
  [messages.append({"role":"user","content": str(i)}) for i in measurements]
  
  response = get_response(messages)
  print(response)
  ```
  
  - Checking number of tokens in input
  ```
  import tiktoken
  client = OpenAI(api_key="<OPENAI_API_TOKEN>")
  input_message = {"role": "user", "content": "I'd like to buy a shirt and a jacket. Can you suggest two color pairings for these items?"}
  
  # Use tiktoken to create the encoding for your model
  encoding = tiktoken.encoding_for_model('gpt-4o-mini')
  # Check for the number of tokens
  num_tokens = len(encoding.encode(input_message['content']))
  
  # Run the chat completions function and print the response
  if num_tokens <= 100:
      response = client.chat.completions.create(model="gpt-4o-mini", messages=[input_message])
      print(response.choices[0].message.content)
  else:
      print("Message exceeds token limit")
  ```

# Authentication error - key expired
```
from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_TOKEN>")
# Use the try statement
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[message]
        )
    # Print the response
    print(response.choices[0].messages.content)
# Use the except statement
except openai.AuthenticationError:
    print(f"Please double check your authentication key and try again, the one provided is not valid.")
```

# Bad request errors 400 - role not in ["system","assistant","user","function"]
  
