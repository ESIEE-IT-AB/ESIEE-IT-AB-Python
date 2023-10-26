import string
import math


class MDP:
    def __init__(self, pwd):
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