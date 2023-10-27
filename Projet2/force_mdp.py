from module_mdp import calcul_entropie


class FORCE_MDP:
    def __init__(self, pwd=""):
        self.mot_de_passe = pwd

    def get_mdp(self):
        return self.mot_de_passe

    def set_mdp(self, mdp):
        self.mot_de_passe = mdp

    def print_mdp(self):
        print(self.mot_de_passe)

    """
    Permet de lancer le test de force du mot de passe
    """
    def test_force_mdp(self):
        print(calcul_entropie(self.get_mdp()))
