import speech_recognition as sr

hot_word = 'sentinel'

def listen_for_hotword():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say 'Sentinel' to activate the assistant...")
        while True:
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()

                if hot_word in command:
                    print("Hotword detected: 'Sentinal'")
                    return True  # Hotword detected, now listen for command

            except sr.UnknownValueError:
                print("Listening...")
            except sr.RequestError:
                print("Could not request results; check your network connection.")

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
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
