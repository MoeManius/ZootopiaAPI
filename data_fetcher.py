# data_fetcher.py
import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

API_URL = os.getenv("API_URL", "https://api.api-ninjas.com/v1/animals")
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {...},
      'locations': [...],
      'characteristics': {...}
    }
    """
    if not API_KEY:
        print("Error: API_KEY not found. Please set it in your .env file.")
        return []

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
