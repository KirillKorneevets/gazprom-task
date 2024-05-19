import pandas as pd
from pydantic import ValidationError

from src.models.response import *

def process_data(data):
    try:
        api_response = ApiResponseModel(**data)
        validated_rows = [RowModel(key1=row[0], key2=row[1], key3=row[2]) for row in api_response.Rows]
    except ValidationError as e:
        print("Validation error:", e)
        raise
    
    columns = api_response.Columns
    rows = [row.dict().values() for row in validated_rows]
    df = pd.DataFrame(rows, columns=columns)
    
    column_mapping = {
        "key1": "document_id",
        "key2": "document_dt",
        "key3": "document_name"
    }
    df.rename(columns=column_mapping, inplace=True)
    
    return df
