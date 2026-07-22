from openai import OpenAI

client = OpenAI(api_key="")

response = client.responses.create(
    model="qwen2.5-coder:7b",
    input="Explain Playwright in one paragraph."
)

print(response.output_text)