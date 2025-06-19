import requests
from dotenv import load_dotenv
import os

load_dotenv()

def translate_word(word, source_lang='DE', target_lang='EN'):
    url = "https://api-free.deepl.com/v2/translate"
    api_key = os.getenv("DEEPL_API_KEY")
    
    if not api_key:
        raise ValueError("API key not found. Please set the DEEPL_API_KEY environment variable.")

    params = {
        'auth_key': api_key,
        'text': word,
        'source_lang': source_lang.upper(),
        'target_lang': target_lang.upper()
    }
    try:
        response = requests.post(url, data=params)
        return response.json()['translations'][0]['text']
    except Exception as e:
        raise f"Error: {e}"