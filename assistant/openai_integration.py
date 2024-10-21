import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(message):
    if message:
        try:
            completion = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "assistant", "content": "You are my personal assistant. well rounded in Engineering, finance and you only give briefe answeres. unless i ask for more detail"},
                    {
                        "role": "user",
                        "content": message  # Using the message from the request
                    }
                ]
            )

            print(completion._request_id)
            # Print the response to the console
            response = completion.choices[0].message.content
            return response

        except Exception as e:
            print(f"Error fetching GPT response: {e}")
            return ''
