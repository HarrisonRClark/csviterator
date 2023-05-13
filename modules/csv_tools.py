import csv
from typing import List

class CSVReader:
    """This class has the single responsibility of reading a CSV file"""
    def __init__(self, filename: str):
        self.filename = filename

    def read_csv(self) -> List[List[str]]:
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data


class CSVWriter:
    """This class has the single responsibility of writing to a CSV file"""
    def __init__(self, filename: str):
        self.filename = filename

    def write_csv(self, data: List[List[str]]):
        with open(self.filename, 'w', newline='') as file:  # add newline=''
            writer = csv.writer(file)
            writer.writerows(data)