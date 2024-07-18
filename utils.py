import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Access the environment variables
summarize_api_key = os.getenv('SUMMARIZE_API_KEY')

def summerize_text(payload):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization":'Bearer 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'}
	
    response = requests.post(API_URL, headers=headers, json=payload)

    return response.json()