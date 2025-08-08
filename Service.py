import requests
import json

API_URL = "https://openrouter.ai/api/v1/chat/completions"
TOKEN_KEY = ""
headers = {
    "Authorization": f"Bearer {TOKEN_KEY}",
    "Content-Type": "application/json",
    # "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    # "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
}

def query(payload):
    response = requests.post(API_URL, headers, json=payload)
    return response.json()

def generate(messages):
    response = query({
        "messages": messages,
        "model": "z-ai/glm-4.5-air:free"
    })
    return response["choices"][0]["message"]["content"]