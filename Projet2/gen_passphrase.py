import random
from file import FILE


class GEN_PASSPHRASE:
    def __init__(self):
        self.passphrase = ""

    def get_passphrase(self):
        return self.passphrase

    def set_passphrase(self, passphrase):
        self.passphrase = passphrase

    def print_passphrase(self):
        print(self.passphrase)

    """
    Permet de lancer 5 dé (1 à 6) et de retourner les resultats concatenés
    """
    def lancer_de(self):
        dice = [1, 2, 3, 4, 5, 6]
        code = ""
        for i in range(5):
            code = code + str((random.choice(dice)))
        return code


    """
    Permet de generer une passephrase via 6 code à 5 chiffre generer automatiquement.
    Chaque code générer aleatoirement correspond a un mot dans un fichier dictionnaire.
    """
    def generate_passphrase(self):
        file = FILE("eff_large_wordlist.txt")
        file.set_file()
        code = []
        passphrase = ""

        for i in range(6):
            code.append(self.lancer_de())

        code.sort()
        line_file = file.search_5code_infile(code)
        file.close_file()

        for i in range(len(line_file)):
            passphrase = passphrase + "-" + line_file[i]

        return passphrase[1:]


    """
    Permet de lancer la generation de la passphrase et de l'afficher.
    """
    def new_passphrase(self):
        passphrase = self.generate_passphrase()
        self.set_passphrase(passphrase)
        self.print_passphrase()
