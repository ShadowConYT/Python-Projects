import requests
from dotenv import load_dotenv
import os

load_dotenv()
os.environ.get("SERP_API_KEY")

BASE_URL = "https://serpapi.com/search.json"
PARAMS = {
    "q": "anime",
    "location": "Chennai, Tamil Nadu, India",
    "hl": "en",
    "gl": "us",
    "api_key": os.environ.get("SERP_API_KEY")
}

response = requests.get(BASE_URL, PARAMS)
results = response.json()


print(results['organic_results'])