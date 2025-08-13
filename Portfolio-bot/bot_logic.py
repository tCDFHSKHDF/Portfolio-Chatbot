from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_model_response(user_input):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": user_input}],
        stream=False
    )
    return response.choices[0].message["content"]

def Tariq_Ahmad_assistant_stream(user_message, prompt="You are a helpful assistant.", model="openai/gpt-oss-120b"):
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_message}
    ]
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        stream=True,
    )
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
