from openai import OpenAI
client = OpenAI(
    
)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful virtual assistant."},
        {
            "role": "user",
            "content": "What is coding"
        }
    ]
)

print(completion.choices[0].message)