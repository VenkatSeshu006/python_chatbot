from openai import OpenAI

client = OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role":"user", "content":"write an explation of how quantum computing works in simple terms"}]
)

print(response.choices[0].message.content)