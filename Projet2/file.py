class FILE:
    def __init__(self, filename=""):
        self.file = ""
        self.filename = filename

    def get_file(self):
        return self.file

    def set_file(self):
        self.file = self.open_file()

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename

    def open_file(self):
        return open(self.filename)

    def close_file(self):
        self.file.close()

    def read_file(self):
        print(self.file.read())

    def readline_file(self):
        print(self.file.readline())

    def search_5code_infile(self, recherche):
        code = []
        lines = self.file.readlines()
        for row in lines:
            for i in range(len(recherche)):
                if recherche[i] in row:
                    code.append((row[6:])[:-1])
        return code