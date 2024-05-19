import requests
from datetime import datetime

def fetch_data_from_api():
    timestamp = int(datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp())
    url = f'https://api.gazprombank.ru/very/important/docs?documents_date={timestamp}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
