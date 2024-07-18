import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Access the environment variables
summarize_api_key = os.getenv('SUMMARIZE_API_KEY')

def summerize_text(payload):
    try:
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization":summarize_api_key}
        
        response = requests.post(API_URL, headers=headers, json=payload)

        return response.json()
    except Exception as e:
        return [{'summary_text': 'There is some issue please try again'}]