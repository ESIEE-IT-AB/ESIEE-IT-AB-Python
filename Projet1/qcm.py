from question import Question
import random


class QCM:
    def __init__(self, package_questions):
        self.questions = package_questions

    """
    Permet de shuffle les questions du QCM.
    """
    def shuffle_qcm(self):
        random.shuffle(self.questions)

    def demande_reponse(self):
        reponse = input("Reponse A, B ou C \n").upper()

        while reponse not in ["A", "B", "C"]:
            if reponse not in ["A", "B", "C"]:
                print("Reponse invalide ! ")
            reponse = input("Reponse A, B ou C \n").upper()

        return reponse


    """
    Lancement du qcm
    """
    def lancement_qcm(self):
        note = 0
        correction = []
        for i in range(len(self.questions)):
            self.questions[i].print_question()
            self.questions[i].print_choix()
            reponse = self.demande_reponse()
            if self.questions[i].correction(reponse) is True:
                print("bien joué !")
                note = note + 1
            elif self.questions[i].correction(reponse) is False:
                print("Faux !")
            correction.append(self.questions[i].get_reponse())

        print("Fin du qcm !")
        print("Vous avez " + str(note) + "/" + str(len(self.questions)))
        print("Voici la correction : ")
        for i in range(len(self.questions)):
            print(correction[i])
