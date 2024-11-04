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
