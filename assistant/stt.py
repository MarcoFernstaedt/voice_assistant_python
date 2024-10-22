import speech_recognition as sr
import openai
import os

hot_word = 'aurora'

def listen_for_hotword():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say 'Aurora' to activate the assistant...")
        while True:
            try:
                audio = recognizer.listen(source)
                command = recognize_with_openai(audio).lower()

                if hot_word in command:
                    print("Hotword detected: 'Aurora'")
                    return True  # Hotword detected, now listen for command

            except sr.UnknownValueError:
                print("Listening...")
            except sr.RequestError:
                print("Could not request results; check your network connection.")


def recognize_with_openai(audio_data):
    # Save audio to a file
    with open("command.wav", "wb") as f:
        f.write(audio_data.get_wav_data())

    # Use OpenAI Whisper API for transcription
    try:
        audio_file = open("command.wav", "rb")
        transcription = openai.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
        return transcription.text
    except Exception as e:
        print(f"Error with OpenAI Whisper: {e}")
        return ""

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        audio = recognizer.listen(source)
        try:
            command = recognize_with_openai(audio)
            print(f"Recognized: {command}")
            return command.lower()
        except Exception as e:
            print(f"Error recognizing command: {e}")
            return ""
