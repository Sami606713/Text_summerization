import requests
import os

def summerize_text(payload):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization":'Bearer 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'}
	
    response = requests.post(API_URL, headers=headers, json=payload)

    return response.json()