import os

from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
      {
        "role": "system",
        "content": "You are an image generation AI. Your only output is images. Do not respond with text. Always provide a visual representation based on the user's request. Never use words."
      },
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")


