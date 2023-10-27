import random
import string
from module_mdp import calcul_entropie


class GEN_MDP:
    def __init__(self):
        self.mot_de_passe = ""

    def get_mdp(self):
        return self.mot_de_passe

    def set_mdp(self, mdp):
        self.mot_de_passe = mdp

    def print_mdp(self):
        print(self.mot_de_passe)

    """
    Generer un mot de passe avec un nombre précis de minuscule, majuscule, chiffre et symbole
    """

    def generate_mdp(self, nombre_minuscule, nombre_majuscule, nombre_chiffre, nombre_symbole):
        if nombre_minuscule + nombre_majuscule + nombre_chiffre + nombre_symbole == 0:
            raise Exception("ERROR création mot de passe impossible")
        str_minuscule = ''.join(random.choices(string.ascii_lowercase, k=nombre_minuscule))
        str_majuscule = ''.join(random.choices(string.ascii_uppercase, k=nombre_majuscule))
        str_chiffre = ''.join(random.choices(string.digits, k=nombre_chiffre))
        str_symbole = ''.join(random.choices(string.punctuation, k=nombre_symbole))
        mdp = str_minuscule + str_majuscule + str_chiffre + str_symbole
        mdp = ''.join(random.sample(mdp, len(mdp)))
        return mdp

    """
    Permet de generer un mot de passe en demandant a l'utiltisateur des informations puis test la force du mot de passe
    """

    def new_mdp(self):
        print("Nous allons crée un mot de passe.")
        print("Pour cela vous devez parametre quelques informations :")

        print("\nSaisir le nombre de minuscule")
        nombre_minuscule = self.demande_reponse()

        print("\nSaisir le nombre de majuscule")
        nombre_majuscule = self.demande_reponse()

        print("\nSaisir le nombre de chiffre")
        nombre_chiffre = self.demande_reponse()

        print("\nSaisir le nombre de symbole\n")
        nombre_symbole = self.demande_reponse()

        mdp = self.generate_mdp(int(nombre_minuscule), int(nombre_majuscule), int(nombre_chiffre), int(nombre_symbole))
        self.set_mdp(mdp)
        print(self.get_mdp())
        print(calcul_entropie(self.get_mdp()))

    def demande_reponse(self):
        while True:
            nombre = input("Choisir un chiffre ou un nombre\n")
            if nombre.isdigit():  # Vérifie si l'entrée est un nombre positif
                return int(nombre)  # Convertit la chaîne en entier et la renvoie
            else:
                print("Invalide !")
