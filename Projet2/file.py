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

    """
    Permet d'ouvrir le fichier via le nom'
    """
    def open_file(self):
        try:
            file = open(self.filename)
        except OSError:
            raise Exception("ERROR impossible d'ouvrir le fichier " + self.filename)
        return file

    """
    Permet de fermer le fichier.
    """
    def close_file(self):
        self.file.close()

    """
    Permet d'afficher le fichier'
    """
    def read_file(self):
        print(self.file.read())

    """
    Permet d'afficher une ligne du fichier'
    """
    def readline_file(self):
        print(self.file.readline())

    """
    Permet de rechercher plusieurs code dans le fichier via une liste et de retourner les mots assciés dans un liste 
    """
    def search_5code_infile(self, recherche):
        code = []
        lines = self.file.readlines()
        for row in lines:
            for i in range(len(recherche)):
                if recherche[i] in row:
                    code.append((row[6:])[:-1])
        return code