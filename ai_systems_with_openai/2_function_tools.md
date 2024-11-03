
Tools are ways to call external functions 
```
from openai import OpenAI
client = OpenAI(api_key="ENTER YOUR KEY HERE")

# first define function that need to be used by openai.
# provide name, description of the function
# give expected output argument details
function_definition = [{
  'type': 'function',
  'function': {
  'name': 'extract_job_info',
  'description': 'Get the job information from the body of the input text',
  'parameters':
    {'type': 'object',
    'properties':
        'job': {'type': 'string',
                'description': 'Job title'},
        'location': {'type': 'string',
                'description': 'Office location'},
    }
  }
]
# usage of function
response= client.chat.completions.create(
  model="gpt-4o-mini",
  messages=messages,
  tools=function_definition,
)
# Now we don't have content in the message directly like earlier
# print(response.choices[0].message.content)
# tool_calls is a list, one for each function provided in the function_definition list
 
print(response.choices[0].message.tool_calls[0].function.arguments)
# example output: {"job":"Data Scientist","location":"San Francisco, CA"}
```

# focrefully calling a particular function
- If function_definition has multiple functions, model will decice which function to call based on the prompt.
- If you want to forcefully call a particular function, use tool_choice argument.
- PS: Default value of tool_choice is "auto"

```
response= client.chat.completions.create(
  model="gpt-4o-mini",
  messages=messages,
  tools=function_definition,
  # Specify the function to be called for the response
  tool_choice={"type":"function",
        "function":{"name":"extract_job_info"}
        }
)
```
