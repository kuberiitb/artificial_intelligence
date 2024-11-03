# erros in openai API library -- 404 - model doesn't exists

# connection errors
- InternalServerError
- APIConnectionError
- APITimeoutError
Solution- Check connection config

# Reduce limitis error
- Conflict error, RateLimitError
Solution: check limit restrictions, ensure rates are in limit.

# Authentication error - key expired   
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

# Bad request errors 400 - role not in ["system","assistant","user","function"]
  
