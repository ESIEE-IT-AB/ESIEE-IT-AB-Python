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

        nombre_minuscule_default = 5
        nombre_majuscule_default = 3
        nombre_chiffre_default = 4
        nombre_symbole_default = 2

        mdp = mdp_instance.generate_mdp(nombre_minuscule_default, nombre_majuscule_default, nombre_chiffre_default, nombre_symbole_default)

        nombre_minuscule = 0
        for char in mdp:
            if char in string.ascii_lowercase:
                nombre_minuscule += 1

        nombre_majuscule = 0
        for char in mdp:
            if char in string.ascii_uppercase:
                nombre_majuscule += 1

        nombre_chiffre = 0
        for char in mdp:
            if char in string.digits:
                nombre_chiffre += 1

        nombre_symbole = 0
        for char in mdp:
            if char in string.punctuation:
                nombre_symbole += 1

        self.assertEqual(nombre_minuscule, nombre_minuscule_default)
        self.assertEqual(nombre_majuscule, nombre_majuscule_default)
        self.assertEqual(nombre_chiffre, nombre_chiffre_default)
        self.assertEqual(nombre_symbole, nombre_symbole_default)

    def input_stub(*args):
        responses = ["2", "2", "2", "2"]
        return responses.pop(0)

    def test_new_mdp(self):
        mdp_instance = MDP()

        original_input = __builtins__.input
        __builtins__.input = self.input_stub

        mdp_instance.new_mdp()

        __builtins__.input = original_input

        self.assertEqual(len(mdp_instance.get_mdp()), 8)

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
