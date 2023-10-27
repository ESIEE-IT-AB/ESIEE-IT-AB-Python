import string
import unittest
from force_mdp import FORCE_MDP
from gen_mdp import GEN_MDP
from gen_passphrase import GEN_PASSPHRASE
from module_mdp import *


class TestMDP(unittest.TestCase):

    def test_calcul_N(self):
        mdp = "10101"
        self.assertEqual(calcul_N(mdp), 2)

        mdp = "12345"
        self.assertEqual(calcul_N(mdp), 10)

        mdp = "1A2B"
        self.assertEqual(calcul_N(mdp), 16)

        mdp = "ABCDEFGHIJ"
        self.assertEqual(calcul_N(mdp), 26)

        mdp = "A1B2HI98"
        self.assertEqual(calcul_N(mdp), 36)

        mdp = "AbCd"
        self.assertEqual(calcul_N(mdp), 52)

        mdp = "Ab1C"
        self.assertEqual(calcul_N(mdp), 62)

        mdp = "A!b1C"
        self.assertEqual(calcul_N(mdp), 70)

        mdp = "A!b1Ç"
        self.assertEqual(calcul_N(mdp), 90)

    def test_calcul_L(self):
        mdp = "10101"
        self.assertEqual(calcul_L(mdp), 5)

        mdp = "123456"
        self.assertEqual(calcul_L(mdp), 6)

    def test_calcul_entropie(self):
        mdp = "10101"
        self.assertEqual(calcul_entropie(mdp)[1], "très faible")

        mdp = "123456789012345678901234"
        self.assertEqual(calcul_entropie(mdp)[1], "faible")

        mdp = "AbCdEfGh12345!"
        self.assertEqual(calcul_entropie(mdp)[1], "moyen")

        mdp = "AbCdEfGh123456789012345678901234567890"
        self.assertEqual(calcul_entropie(mdp)[1], "fort")

    def test_generate_mdp(self):
        mdp_instance = GEN_MDP()

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
        mdp_instance = GEN_MDP()

        original_input = __builtins__.input
        __builtins__.input = self.input_stub

        mdp_instance.new_mdp()

        __builtins__.input = original_input

        self.assertEqual(len(mdp_instance.get_mdp()), 8)

    def test_lancer_de(self):
        mdp = GEN_PASSPHRASE()
        for i in range(100):
            code = mdp.lancer_de()
            self.assertEqual(len(code), 5)
            for char in code:
                self.assertTrue(1 <= int(char) <= 6)

    def test_generate_passphrase(self):
        mdp = GEN_PASSPHRASE()
        passphrase = mdp.generate_passphrase()
        self.assertIsInstance(passphrase, str)


if __name__ == '__main__':
    unittest.main()
