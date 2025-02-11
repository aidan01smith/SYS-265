import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API credentials
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Debugging: Print to check if values are loaded
print("Consumer Key:", CONSUMER_KEY)
print("Consumer Secret:", CONSUMER_SECRET)
