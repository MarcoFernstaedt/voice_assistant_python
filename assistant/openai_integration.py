import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(message):
    if message:
        try:
            response = openai.Completion.create(
                model="gpt-4",
                messages=[
                    {"role": "assistant", "content": "You are my personal assistant. well rounded in Engineering, finance and you only give brief answers unless I ask for more detail."},
                    {"role": "user", "content": message}
                ]
            )
            return response.choices[0].message['content']
        except Exception as e:
            print(f"Error fetching GPT response: {e}")
            return ''
