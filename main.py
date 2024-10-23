import logging
from assistant.stt import listen_for_hotword, listen_for_command  
from assistant.openai_integration import get_openai_response
from assistant.tts import speak
from assistant.command_handler import handle_spotify_commands

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

awake = True

if __name__ == "__main__":
    try:
        while awake:
            if listen_for_hotword():  # Wait for the hotword
                command = listen_for_command()  # Then listen for the actual command
                if command:
                    if 'stop' not in command:
                        if 'spotify' in command:
                            handle_spotify_commands(command)
                        else:
                            response = get_openai_response(command)  # Send command to OpenAI:
                            if response:
                                logger.info(f"Assistant response: {response}")
                                speak(response)  # Speak the response
                            else:
                                logger.warning('No valid response from OpenAI.')
                    else:
                        logger.info('Assistant shutting down...')
                        speak('Shutting down. Goodbye!')
                        awake = False
                else:
                    logger.warning('No command recognized.')
    except Exception as e:
        logger.error(f"An error occurred: {e}")
