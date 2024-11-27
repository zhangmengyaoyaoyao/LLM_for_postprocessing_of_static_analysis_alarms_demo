from openai import OpenAI
import openai 
import os
#client = OpenAI()
os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

openai.api_key="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",
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