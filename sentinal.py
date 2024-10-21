import speech_recognition as sr
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Recognized: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return ""
        
def get_openai_responce(message):
    if message:
        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "assistant", "content": "You are my personal assistant. well rounded in Engineering, finance and you only give briefe answeres. unless i ask for more detail"},
                    {
                        "role": "user",
                        "content": message  # Using the message from the request
                    }
                ]
            )

            print(response._request_id)
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error fetching GPT response: {e}")
            return ''

# Test the function
if __name__ == "__main__":
    command = listen_for_command()
    if command:
        responce = get_openai_responce(command)
        print('Assistant: ' + responce)
