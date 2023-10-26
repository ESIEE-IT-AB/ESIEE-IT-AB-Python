import string
import random
import math
from file import *

class MDP:
    def __init__(self, pwd=""):
        self.mot_de_passe = pwd

    def calcul_N(self):
        # binaire
        binaire = True
        for char in self.mot_de_passe:
            if char not in '01':
                binaire = False
                break
        if binaire:
            return 2

        # décimal
        decimal = True
        for char in self.mot_de_passe:
            if char not in '0123456789':
                decimal = False
                break
        if decimal:
            return 10

        # hexadécimal
        hexadecimal = True
        for char in self.mot_de_passe:
            if char not in '0123456789ABCDEF':
                hexadecimal = False
                break
        if hexadecimal:
            return 16

        # alphabétique majuscule
        alphabetique_majuscule = True
        for char in self.mot_de_passe:
            if char not in string.ascii_uppercase:
                alphabetique_majuscule = False
                break
        if alphabetique_majuscule:
            return 26

        # alphanumérique majuscule
        alphanumerique_majuscule = True
        for char in self.mot_de_passe:
            if char not in (string.digits + string.ascii_uppercase):
                alphanumerique_majuscule = False
                break
        if alphanumerique_majuscule:
            return 36

        # alphabétique (majuscules et minuscules)
        alphabetique_majuscules_minuscules = True
        for char in self.mot_de_passe:
            if char not in string.ascii_letters:
                alphabetique_majuscules_minuscules = False
                break
        if alphabetique_majuscules_minuscules:
            return 52

        # alphanumérique (majuscules, minuscules et chiffres)
        alphanumerique_majuscules_minuscules_chiffres = True
        for char in self.mot_de_passe:
            if char not in (string.digits + string.ascii_letters):
                alphanumerique_majuscules_minuscules_chiffres = False
                break
        if alphanumerique_majuscules_minuscules_chiffres:
            return 62

        # alphanumérique étendu avec symboles
        alphanumerique_etendu_avec_symboles = True
        for char in self.mot_de_passe:
            if char not in (string.digits + string.ascii_letters + '!#$%?'):
                alphanumerique_etendu_avec_symboles = False
                break
        if alphanumerique_etendu_avec_symboles:
            return 70

        # Sinon plus puissant
        return 90

    def calcul_L(self):
        return len(self.mot_de_passe)

    def test_force_mdp(self):
        print(self.calcul_entropie())

    def calcul_entropie(self):
        L = self.calcul_L()
        N = self.calcul_N()

        entropie = L * math.log2(N)

        if entropie <= 64:
            return "très faible"
        elif 64 < entropie <= 80:
            return "faible"
        elif 80 < entropie <= 100:
            return "moyen"
        else:
            return "fort"

    def get_mdp(self):
        return self.mot_de_passe

    def set_mdp(self, mdp):
        self.mot_de_passe = mdp

    def print_mdp(self):
        print(self.mot_de_passe)

    def generate_mdp(self, nombre_minuscule, nombre_majuscule, nombre_chiffre, nombre_symbole):
        str_minuscule = ''.join(random.choices(string.ascii_lowercase, k=nombre_minuscule))
        str_majuscule = ''.join(random.choices(string.ascii_uppercase, k=nombre_majuscule))
        str_chiffre = ''.join(random.choices(string.digits, k=nombre_chiffre))
        str_symbole = ''.join(random.choices(string.punctuation, k=nombre_symbole))
        mdp = str_minuscule + str_majuscule + str_chiffre + str_symbole
        mdp = ''.join(random.sample(mdp, len(mdp)))
        return mdp

    def new_mdp(self):
        print("Nous allons crée un mot de passe.")
        print("Pour cela vous devez parametre quelques informations :")
        nombre_minuscule = input("Saisir le nombre de minuscule\n")
        nombre_majuscule = input("Saisir le nombre de majuscule\n")
        nombre_chiffre = input("Saisir le nombre de chiffre\n")
        nombre_symbole = input("Saisir le nombre de symbole\n")
        mdp = self.generate_mdp(int(nombre_minuscule), int(nombre_majuscule), int(nombre_chiffre), int(nombre_symbole))
        self.set_mdp(mdp)
        print(self.get_mdp())
        self.test_force_mdp()

    def lancer_de(self):
        dice = [1, 2, 3, 4, 5, 6]
        code = ""
        for i in range(5):
            code = code + str((random.choice(dice)))
        return code

    def new_passphrase(self):
        file = open_file("eff_large_wordlist.txt")
        code = []
        passphrase = ""
        for i in range(6):
            code.append(self.lancer_de())

        code.sort()
        line_file = search_5code_infile(file, code)
        close_file(file)

        for i in range(len(line_file)):
            passphrase = passphrase + line_file[i]

        print(passphrase)

