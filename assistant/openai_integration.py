import openai
import os
import time
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Specify your existing Assistant ID and Thread ID 
assistant_id = os.getenv('ASSISTANT_ID')
thread_id = os.getenv('THREAD_ID')

def get_nova_response(message):
    global thread_id  # Update global thread_id for future calls
    if message:
        try:
            # Check if thread_id is valid
            if not thread_id:  # If no existing thread
                # Create a new thread
                thread = openai.beta.threads.create()
                thread_id = thread.id

            # Add the user message to the thread
            openai.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=message
            )

            # Create and run the thread to get a response
            run = openai.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=assistant_id
            )

            # Monitor the run status
            while True:
                # Fetch the current status of the run
                run_status = openai.beta.threads.runs.retrieve(run.id, thread_id=thread_id)  # Retrieve the run to check status
                if run_status.status == 'completed':
                    logger.info('Run completed')
                    break
                elif run_status.status == 'failed':
                    logger.error('Run failed')
                    return 'Run failed'
                time.sleep(0.3)

            # Once completed, extract and return the response
            thread_message = openai.beta.threads.messages.list(thread_id)
            return  thread_message.data[0].content[0].text.value

        except openai.error.OpenAIError as e:
            logger.error(f"OpenAI API error: {e}")
            return ''
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return ''

# Example usage
# response = get_nova_response("Can you help me with a math problem?")
# print(response)