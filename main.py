class CSVCreator:
    def __init__(self):
        self.data_path = './data.txt'
        self.csv_path = './data.csv'
        
    def cast_to_csv(self, separator: str = ' '):
        with open(self.data_path, 'r') as file:
            lines = file.readlines()
            with open(self.csv_path, 'w') as csv_file:
                for line in lines:
                    csv_file.write(line.replace(separator, ','))


if __name__ == '__main__':
    csv_creator = CSVCreator()
    separator = input("Enter the separator in txt file: ")
    if len(separator) > 1:
        raise ValueError("Separator must be a single character")
    csv_creator.cast_to_csv(separator=separator)
