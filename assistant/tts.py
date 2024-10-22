# from gtts import gTTS
import os
from pathlib import Path
import openai

def speak(text):
    # Set the path where the audio file will be saved
    speech_file_path = Path(__file__).parent / "speech.mp3"
    
    try:
        # Call OpenAI TTS API to generate audio
        response = openai.audio.speech.create(
            model="tts-1",          # Model to use (standard model)
            voice="onyx",           # Voice to use (you can choose: alloy, echo, fable, onyx, nova, shimmer)
            input=text              # The text to be converted to speech
        )
        
        # Stream the response to an MP3 file
        response.stream_to_file(speech_file_path)
        
        # Play the generated MP3 file
        print(f"Playing generated audio: {speech_file_path}")
        os.system(f"afplay {speech_file_path}")  # Use 'afplay' for MacOS, 'start' for Windows

    except Exception as e:
        print(f"Error generating speech: {e}")

    
    
    # tts = gTTS(text=text, lang='en')
    # tts.save('response.mp3')
    # os.system("afplay response.mp3")
