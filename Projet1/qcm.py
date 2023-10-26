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
            self.questions[i].shuffle_reponse()

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
        correction_save = []
        question_save = []

        for question in self.questions:
            print(question.get_question())

            reponse = question.get_reponse()
            print("A : " + reponse[0])
            print("B : " + reponse[1])
            print("C : " + reponse[2])

            reponse_user = self.demande_reponse()
            match reponse_user:
                case "A":
                    if question.correction(reponse[0]):
                        note += 1
                        print("Bien joué !\n")
                    else:
                        print("Faux !\n")
                case "B":
                    if question.correction(reponse[1]):
                        note += 1
                        print("Bien joué !\n")
                    else:
                        print("Faux !\n")
                case "C":
                    if question.correction(reponse[2]):
                        note += 1
                        print("Bien joué !\n")
                    else:
                        print("Faux !\n")

            question_save.append(question.get_question())
            correction_save.append(question.get_reponse_correct())

        print("Fin du qcm !")
        print("Vous avez " + str(note) + "/" + str(len(self.questions)))
        print("Voici la correction : \n")
        for i in range(len(self.questions)):
            print(question_save[i])
            print(correction_save[i]+"\n\n")
