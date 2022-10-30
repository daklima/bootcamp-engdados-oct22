import os
import datetime
import json
from typing import List


class DataTypeNotSupportedForIngestionException(Exception):
    def __init__(self, data):
        self.data = data
        self.message = f'Data type {type(data)} is not supported for ingestion.'
        super().__init__(self.message)

class DataWriter:
    def __init__(self, coin: str, api: str) -> None:
        self.coin = coin
        self.api = api
        self.filename = f'{self.api}/{self.coin}/{datetime.datetime.now()}.json'.replace(":", "-")

    def _write_row(self, row: str):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, 'a') as f:
            f.write(row)
    
    def write(self, data: [List, dict]):
        if isinstance(data, dict):
            self._write_row(json.dumps(data) +'\n')
        elif isinstance(data, List):
             for d in data:
                 self.write(d)
        else:
            raise DataTypeNotSupportedForIngestionException(data)
