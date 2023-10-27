from question import Question
from reponse import Reponse
from qcm import QCM

print("Bienvenue dans ce QMC sur Python")
print("Le QCM est noté sur 10 points soit 1 point par question")
print("Vous trouverez votre score et la correction aux questions à la fin du QCM")
print("\nBonne chance !\n")

questions = [
    Question("Python est un langage _______", [Reponse("interprété", True), Reponse("compilé"), Reponse("machine")]),
    Question("Quel est la bonne syntaxe pour ecrire sur la sortie standard en Python", [Reponse("echo \'bonjour\'", True), Reponse("print(\"bonjour\")"), Reponse("printf(\"bonjour\")")]),
    Question("En python 3, que fait l’opérateur //", [Reponse("Division entière", True), Reponse("Retourne le reste"), Reponse("Division du float par zéro")]),
    Question("En python, quel mot clé est utilisé pour commencer une fonction", [Reponse("function"), Reponse("def", True), Reponse("import")]),
    Question("Quelle sera la sortie du code suivant: print type(type(int))", [Reponse("type int"), Reponse("type type", True), Reponse("Error")]),
    Question("Quelle est la sortie pour 'python' [-3]", [Reponse("h", True), Reponse("t"), Reponse("o")]),
    Question("Quel est la bonne syntaxe pour ecrire sur la sortie standard en Python", [Reponse("Module"), Reponse("Classe"), Reponse("Méthode", True)]),
    Question("Supposons que list1 est [2, 3, 4, 5, 1, 20, 6], quelle sera la valeur de list1 après list1.pop(1)", [Reponse("[2, 1, 4, 5, 1, 20, 6]"), Reponse("[2, 4, 5, 1, 20, 6]", True), Reponse("[2, 3, 4, 5, 1, 20, 6, 1]")]),
    Question("Quel opérateur est surchargé par la fonction or()?", [Reponse("//"), Reponse("||"), Reponse("|", True)]),
    Question("Comment je m'appelle ?", [Reponse("Antoine", True), Reponse("Julien"), Reponse("Jeremy")])
]

mon_qcm = QCM(questions)
mon_qcm.shuffle_qcm()
mon_qcm.lancement_qcm()

print("QCM terminé merci d'avoir essayer, aurevoir")
