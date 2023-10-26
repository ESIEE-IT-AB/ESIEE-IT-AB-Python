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


if __name__ == '__main__':
    unittest.main()
