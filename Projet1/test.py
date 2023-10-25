import unittest
from question import Question
from qcm import QCM


class TestQuestion(unittest.TestCase):

    def setUp(self):
        self.question = Question("Python est un langage _______", "interprété", "compilé", "machine", "interprété")

    def test_correction(self):
        self.assertTrue(self.question.correction("interprété"))
        self.assertFalse(self.question.correction("compilé"))

    def test_get_reponse(self):
        self.assertEqual(self.question.get_reponse(), "interprété")

    def test_get_choix(self):
        self.assertEqual(self.question.get_choix(), ["interprété", "compilé", "machine"])

    def test_get_question(self):
        self.assertEqual(self.question.get_question(), "Python est un langage _______")

    def test_shuffle_choix(self):
        choix_default = self.question.get_choix()
        self.question.shuffle_choix()
        choix_shuffled = self.question.get_choix()
        self.assertCountEqual(choix_default, choix_shuffled)


class TestQCM(unittest.TestCase):

    def setUp(self):
        self.questions = [
            Question("Python est un langage _______", "interprété", "compilé", "machine", "interprété"),
            Question("Quel est la bonne syntaxe pour ecrire sur la sortie standard en Python", "echo \'bonjour\'",
                     "print(\"bonjour\")", "printf(\"bonjour\")", "print(\"bonjour\")"),
            Question("En python 3, que fait l’opérateur //", "Division entière", "Retourne le reste",
                     "Division du float par zéro", "Division entière"),
            Question("En python, quel mot clé est utilisé pour commencer une fonction", "function", "def", "import",
                     "def"),
            Question("Quelle sera la sortie du code suivant: print type(type(int))", "type int", "type type", "Error",
                     "type type"),
            Question("Quelle est la sortie pour 'python' [-3]", "h", "t", "o", "h"),
            Question("Quel est la bonne syntaxe pour ecrire sur la sortie standard en Python", "Module", "Classe",
                     "Méthode", "Méthode"),
            Question(
                "Supposons que list1 est [2, 3, 4, 5, 1, 20, 6], quelle sera la valeur de list1 après list1.pop(1)",
                "[2, 1, 4, 5, 1, 20, 6]", "[2, 4, 5, 1, 20, 6]", "[2, 3, 4, 5, 1, 20, 6, 1]", "[2, 4, 5, 1, 20, 6]"),
            Question("Quel opérateur est surchargé par la fonction or()?", "//", "||", "|", "|"),
            Question("Comment je m'appelle ?", "Antoine", "Julien", "Jeremy", "Antoine")
        ]
        self.qcm = QCM(self.questions)

    def test_shuffle_qcm(self):
        liste_default = []
        for question in self.qcm.questions:
            liste_default.append(question.get_question())

        self.qcm.shuffle_qcm()
        liste_shuffled = []
        for question in self.qcm.questions:
            liste_shuffled.append(question.get_question())

        questions_changed = False
        for i in range(len(liste_default)):
            question_default = liste_default[i]
            question_shuffled = liste_shuffled[i]
            if question_default != question_shuffled:
                questions_changed = True
                break

        self.assertTrue(questions_changed)


if __name__ == '__main__':
    unittest.main()
