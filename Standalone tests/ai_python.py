from openai import OpenAI

client = OpenAI(api_key="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")

response = client.responses.create(
    model="qwen2.5-coder:7b",
    input="Explain Playwright in one paragraph."
)

print(response.output_text)