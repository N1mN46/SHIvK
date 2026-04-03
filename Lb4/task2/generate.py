from ollama import generate

response = generate('deepseek-r1:8b', 'Why do zebras have black stripes on their bodies?')
print(response['response'])