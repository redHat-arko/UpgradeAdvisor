class TXTParser:
    def __init__(self):
        self.parts = []

    def parse(self, filename):
        with open(filename, 'r') as file:
            lines = [line.rstrip() for line in file]

        for i in range(1, 3):
            part = lines[i][5:]
            part = part[: part.rfind('-')].rstrip()
            self.parts.append(part)

        return self.parts[0], self.parts[1]