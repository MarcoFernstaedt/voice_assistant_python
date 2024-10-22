import openai
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(message):
    if message:
        try:
            # Fetch GPT completion
            completion = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "assistant", "content": "You are my personal assistant. well rounded in Engineering, finance and you only give brief answers. unless I ask for more detail."},
                    {
                        "role": "user",
                        "content": message  # Using the message from the request
                    }
                ]
            )

            # Log request ID for tracking
            logger.info(f"Request ID: {completion._request_id}")

            # Extract and return the response
            response = completion.choices[0].message.content
            return response

        except openai.error.OpenAIError as e:
            logger.error(f"OpenAI API error: {e}")
            return ''
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return ''
