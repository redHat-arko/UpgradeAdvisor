import csv


class CSVParser:
    def __init__(self):
        self.names = []
        self.scores = []

    def parse(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                self.names.append(row[2] + ' ' + row[3])
                self.scores.append(float(row[5]))

        return self.names, self.scores
