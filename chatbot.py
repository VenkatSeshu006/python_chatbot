from google import genai


client = genai.Client(api_key="AQ.Ab8RN6JMuTXxyX5JEFN2_tblEsoFJWLFtRTsq7uTiYcYd311pQ")



print("Gemini Chatbot Started!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
    )

    print("Bot:", response.text)