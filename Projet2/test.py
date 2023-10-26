import string
import unittest
from mdp import MDP


class TestMDP(unittest.TestCase):

    def test_calcul_N(self):
        mdp = MDP("10101")
        self.assertEqual(mdp.calcul_N(), 2)

        mdp = MDP("12345")
        self.assertEqual(mdp.calcul_N(), 10)

        mdp = MDP("1A2B")
        self.assertEqual(mdp.calcul_N(), 16)

        mdp = MDP("ABCDEFGHIJ")
        self.assertEqual(mdp.calcul_N(), 26)

        mdp = MDP("A1B2HI98")
        self.assertEqual(mdp.calcul_N(), 36)

        mdp = MDP("AbCd")
        self.assertEqual(mdp.calcul_N(), 52)

        mdp = MDP("Ab1C")
        self.assertEqual(mdp.calcul_N(), 62)

        mdp = MDP("A!b1C")
        self.assertEqual(mdp.calcul_N(), 70)

        mdp = MDP("A!b1Ç")
        self.assertEqual(mdp.calcul_N(), 90)

    def test_calcul_L(self):
        mdp = MDP("10101")
        self.assertEqual(mdp.calcul_L(), 5)

        mdp = MDP("123456")
        self.assertEqual(mdp.calcul_L(), 6)

    def test_calcul_entropie(self):
        mdp = MDP("10101")
        self.assertEqual(mdp.calcul_entropie(), "très faible")

        mdp = MDP("123456789012345678901234")
        self.assertEqual(mdp.calcul_entropie(), "faible")

        mdp = MDP("AbCdEfGh12345!")
        self.assertEqual(mdp.calcul_entropie(), "moyen")

        mdp = MDP("AbCdEfGh123456789012345678901234567890")
        self.assertEqual(mdp.calcul_entropie(), "fort")

    def test_generate_mdp(self):
        mdp_instance = MDP()

        nombre_minuscule = 5
        nombre_majuscule = 3
        nombre_chiffre = 4
        nombre_symbole = 2

        mdp = mdp_instance.generate_mdp(nombre_minuscule, nombre_majuscule, nombre_chiffre, nombre_symbole)

        count_minuscule = 0
        for char in mdp:
            if char in string.ascii_lowercase:
                count_minuscule += 1
                
        count_majuscule = 0
        for char in mdp:
            if char in string.ascii_uppercase:
                count_majuscule += 1

        count_chiffre = 0
        for char in mdp:
            if char in string.digits:
                count_chiffre += 1

        count_symbole = 0
        for char in mdp:
            if char in string.punctuation:
                count_symbole += 1

        self.assertEqual(count_minuscule, nombre_minuscule)
        self.assertEqual(count_majuscule, nombre_majuscule)
        self.assertEqual(count_chiffre, nombre_chiffre)
        self.assertEqual(count_symbole, nombre_symbole)

    # Ce test est pour la méthode interactive new_mdp.
    # Vous pourriez avoir besoin de mocker les appels d'entrée pour le rendre non interactif.
    def test_new_mdp(self):
        # Ici, vous pourriez utiliser le module `unittest.mock` pour mocker la fonction `input`.
        pass

    def test_lancer_de(self):
        mdp = MDP()
        for i in range(100):
            code = mdp.lancer_de()
            self.assertEqual(len(code), 5)
            for char in code:
                self.assertTrue(1 <= int(char) <= 6)

    def test_generate_passphrase(self):
        mdp = MDP()
        passphrase = mdp.generate_passphrase()
        self.assertIsInstance(passphrase, str)

if __name__ == '__main__':
    unittest.main()
