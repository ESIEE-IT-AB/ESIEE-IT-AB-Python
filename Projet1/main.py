from question import Question
from qcm import QCM

questions = [
    Question("Python est un langage _______", "interprété", "compilé", "machine", "A"),
    Question("Quel est la bonne syntaxe pour ecrire sur la sortie standard en Python", "echo \'bonjour\'", "print(\"bonjour\")", "printf(\"bonjour\")", "B"),
    Question("En python 3, que fait l’opérateur //", "Division entière", "Retourne le reste", "Division du float par zéro", "A"),
    Question("En python, quel mot clé est utilisé pour commencer une fonction", "function", "def", "import", "B"),
    Question("Quelle sera la sortie du code suivant: print type(type(int))", "type int", "type type", "Error", "B"),
    Question("Quelle est la sortie pour 'python' [-3]", "h", "t", "o", "A"),
    Question("Quel est la bonne syntaxe pour ecrire sur la sortie standard en Python", "Module", "Classe", "Méthode", "C"),
    Question("Supposons que list1 est [2, 3, 4, 5, 1, 20, 6], quelle sera la valeur de list1 après list1.pop(1)", "[2, 1, 4, 5, 1, 20, 6]", "[2, 4, 5, 1, 20, 6]", "[2, 3, 4, 5, 1, 20, 6, 1]", "B"),
    Question("Quel opérateur est surchargé par la fonction or()?", "//", "||", "|", "C"),
    Question("Comment je m'appelle ?", "Antoine", "Julien", "Jeremy", "A")
]

mon_qcm = QCM(questions)
mon_qcm.shuffle_qcm()
mon_qcm.lancement_qcm()