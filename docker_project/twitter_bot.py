import tweepy
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API credentials from environment variables
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# DeepSeek API URL
DEEPSEEK_API_URL = "http://docker01-aidan:11434/api/generate"

# Configure Tweepy OAuth 1 authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth, wait_on_rate_limit=True)

def get_deepseek_response(prompt):
    """Send a prompt to DeepSeek and retrieve the generated response."""
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False
    }
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("response", "No response from DeepSeek")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to DeepSeek API: {e}")
        return None

def post_tweet():
    """Fetch a response from DeepSeek and tweet it."""
    prompt = "Write a motivational quote."
    deepseek_response = get_deepseek_response(prompt)

    if deepseek_response:
        try:
            twitter_api.update_status(deepseek_response)
            print("Tweet posted successfully!")
        except tweepy.TweepError as e:
            print(f"Error posting tweet: {e}")

if __name__ == "__main__":
    post_tweet()
