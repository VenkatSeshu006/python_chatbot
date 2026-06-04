from openai import OpenAI

client = OpenAI(api_key=" ")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role":"user", "content":"write an explation of how quantum computing works in simple terms"}]
)

print(response.choices[0].message.content)