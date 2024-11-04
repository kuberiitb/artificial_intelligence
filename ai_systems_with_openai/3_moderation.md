# OpenaAI Moderation API flags if user input belongs to one of these
- hate
- harrasment
- self-harm
- sexual
- violence

```
moderation_response = client.moderation.create(input="""
Feeling like killing someone
""")
print(moderation_response.results[0].categories.violence)
# True
```

# prompt injection solution
- limitting amount of text in prompt
- limiting output tokens
- Using pre-selected content as validated input and output

# Adding guardrails
- add a system message adding boudaries like reply with x, y, z if ... else reply "Aplogoies, I don't understand"
