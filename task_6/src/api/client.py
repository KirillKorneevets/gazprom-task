import requests
from datetime import datetime

def fetch_data_from_api():
    timestamp = int(datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp())
    url = f'https://api.gazprombank.ru/very/important/docs?documents_date={timestamp}'
    
    try:
        response = requests.get(url, timeout=10) 
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.ConnectionError:
        print("Connection error")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

    return None
