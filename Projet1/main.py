from question import Question
from qcm import QCM

questions = [
    Question("Python est un langage _______", "interprété", "compilé", "machine", "interprété"),
    Question("Quel est la bonne syntaxe pour ecrire sur la sortie standard en Python", "echo \'bonjour\'", "print(\"bonjour\")", "printf(\"bonjour\")", "print(\"bonjour\")"),
    Question("En python 3, que fait l’opérateur //", "Division entière", "Retourne le reste", "Division du float par zéro", "Division entière"),
    Question("En python, quel mot clé est utilisé pour commencer une fonction", "function", "def", "import", "def"),
    Question("Quelle sera la sortie du code suivant: print type(type(int))", "type int", "type type", "Error", "type type"),
    Question("Quelle est la sortie pour 'python' [-3]", "h", "t", "o", "h"),
    Question("Quel est la bonne syntaxe pour ecrire sur la sortie standard en Python", "Module", "Classe", "Méthode", "Méthode"),
    Question("Supposons que list1 est [2, 3, 4, 5, 1, 20, 6], quelle sera la valeur de list1 après list1.pop(1)", "[2, 1, 4, 5, 1, 20, 6]", "[2, 4, 5, 1, 20, 6]", "[2, 3, 4, 5, 1, 20, 6, 1]", "[2, 4, 5, 1, 20, 6]"),
    Question("Quel opérateur est surchargé par la fonction or()?", "//", "||", "|", "|"),
    Question("Comment je m'appelle ?", "Antoine", "Julien", "Jeremy", "Antoine")
]

mon_qcm = QCM(questions)
mon_qcm.shuffle_qcm()
mon_qcm.lancement_qcm()