from openai import OpenAI

client = OpenAI(api_key="YOUR OPENAI KEY")

repsonse = client.chat.completions.create(
	model = "gpt-4o-mini",
	message = [
		{"role": "user",
		"content": "Who developed ChatGPT?"}
	],
	response_format={"type":"json_object"}
)
print(response.choices[0].message.content)
# ChatGPT was developed by OpenAI
