from datetime import datetime

from src.api.client import fetch_data_from_api
from src.utils.data_processing import process_data


def main():
    data = fetch_data_from_api()
    df = process_data(data)
    df['load_dt'] = datetime.now()
    print(df)

if __name__ == "__main__":
    main()
