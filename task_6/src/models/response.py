from pydantic import BaseModel
from typing import List, Any
from datetime import datetime


class ApiResponseModel(BaseModel):
    Columns: List[str]
    Description: str
    RowCount: int
    Rows: List[List[Any]]

class RowModel(BaseModel):
    key1: int
    key2: datetime
    key3: str
