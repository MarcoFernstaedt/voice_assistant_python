from assistant.stt import listen_for_hotword, listen_for_command  
from assistant.openai_integration import get_openai_response
from assistant.tts import speak

if __name__ == "__main__":
    if listen_for_hotword():  # Wait for the hotword
        command = listen_for_command()  # Then listen for the actual command
        if command:
            response = get_openai_response(command)  # Send command to OpenAI
            if response:
                print(f"Assistant: {response}")
                speak(response)  # Speak the response
            else:
                print('No Valid responce from openAI')
