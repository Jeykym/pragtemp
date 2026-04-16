import requests
from dotenv import load_dotenv
import os
from urllib.parse import urljoin
import json

BASE_URL = 'https://api.golemio.cz'
ENDPOINT = '/v2/microclimate/locations'
API_KEY_NAME = 'API_KEY'
API_KEY_HEADER_NAME = 'X-Access-Token'

load_dotenv()

API_KEY = os.getenv(API_KEY_NAME)
if not API_KEY:
    raise ValueError(f'API key named "{API_KEY_NAME}" is not set in .env')

response = requests.get(
    urljoin(BASE_URL, ENDPOINT),
    headers={API_KEY_HEADER_NAME: API_KEY}
)
print(json.dumps(response.json(), indent=2))