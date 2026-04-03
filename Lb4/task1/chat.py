from ollama import chat

messages = [
    {
        'role': 'user',
        'content': 'Why do zebras have black stripes on their bodies?',
    },
]

response = chat('deepseek-r1:8b', messages=messages)
print(response['message']['content'])