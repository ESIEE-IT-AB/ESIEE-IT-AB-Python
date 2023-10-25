from question import Question
import random


class QCM:
    def __init__(self, package_questions):
        self.questions = package_questions

    """
    Permet de shuffle les questions et les choix du QCM.
    """
    def shuffle_qcm(self):
        random.shuffle(self.questions)
        for i in range(len(self.questions)):
            self.questions[i].shuffle_choix()

    """
    Permet de demander a l'utilisateur la reponse. 
    Si la reponse n'est pas A, a, B, b, C, c on demande a l'utilisateur une nouvelle reponse.
    Une fois la reponse valide on la RETURN
    """
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
            print(self.questions[i].get_question())
            
            choix = self.questions[i].get_choix()
            print("A : " + choix[0])
            print("B : " + choix[1])
            print("C : " + choix[2])

            reponse = self.demande_reponse()
            match reponse:
                case "A":
                    if self.questions[i].correction(choix[0]) is True:
                        note = note + 1
                        print("Bien joué !\n")
                    else:
                        print("Faux !\n")
                case "B":
                    if self.questions[i].correction(choix[1]) is True:
                        note = note + 1
                        print("Bien joué !\n")
                    else:
                        print("Faux !\n")
                case "C":
                    if self.questions[i].correction(choix[2]) is True:
                        note = note + 1.
                        print("Bien joué !\n")
                    else:
                        print("Faux !\n")

            correction.append(self.questions[i].get_reponse())

        print("Fin du qcm !")
        print("Vous avez " + str(note) + "/" + str(len(self.questions)))
        print("Voici la correction : ")
        for i in range(len(self.questions)):
            print(correction[i])
