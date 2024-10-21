from assistant.stt import listen_for_command
from assistant.tts import speak
from assistant.openai_integration import get_openai_response

def process_command():
    command = listen_for_command()
    if command:
        response = get_openai_response(command)
        if response:
            print('Assistant: ' + response)
            speak(response)
