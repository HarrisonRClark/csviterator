from modules.csv_tools import CSVReader, CSVWriter
from modules.combination_generator import CombinationGenerator

class Application:
    """This is the high-level module that uses (CSVReader, CSVWriter, CombinationGenerator)"""
    def __init__(self, input_filename: str, output_filename: str):
        self.reader = CSVReader(f"data/{input_filename}")
        self.writer = CSVWriter(f"data/{output_filename}")
        self.generator = CombinationGenerator()

    def process(self):
        data = self.reader.read_csv()
        combinations = self.generator.generate_combinations(data)
        self.writer.write_csv(combinations)


if __name__ == '__main__':
    app = Application('login.csv', 'output_login.csv')
    app.process()
