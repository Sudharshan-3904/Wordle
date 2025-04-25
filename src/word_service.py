import requests
import random

def get_random_word():
    """Fetch a random 5-letter word from an API"""
    try:
        response = requests.get('https://random-word-api.herokuapp.com/word?length=5')
        if response.status_code == 200:
            return response.json()[0].lower()
    except:
        # Fallback words if API fails
        fallback_words = ['happy', 'world', 'sunny', 'cloud', 'brain']
        return random.choice(fallback_words)