from google import genai 


question = input("Ask AI anything: ")

response = client.chat.completions.create(
    model="genai",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

print("\nAI Response:\n")
print(response.choices[0].message.content)