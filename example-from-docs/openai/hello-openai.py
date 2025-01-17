import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set the API key for OpenAI
openai.api_key = OPENAI_API_KEY

# Create a chat completion
completion = openai.ChatCompletion.create(
    model="gpt-4",  # Corrected model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},  # Changed role to 'system'
        {"role": "user", "content": "Hello!"}
    ]
)

# Print the assistant's response
print(completion.choices[0].message['content'])
