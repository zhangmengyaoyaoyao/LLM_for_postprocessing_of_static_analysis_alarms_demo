from openai import OpenAI
import openai 
import os
os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

# your api key
openai.api_key="",
client = OpenAI(api_key=openai.api_key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    temperature=0.1,
    top_p=0.1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "how can you help me?"
        }
    ]
)

print(completion.choices[0].message)