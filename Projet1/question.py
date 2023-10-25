import random


class Question:
    def __init__(self, question, choix1, choix2, choix3, reponse):
        self.question = question
        self.choix = [choix1, choix2, choix3]
        self.reponse = reponse

    """
    Permet de connaitre si la reponse de l'utilisateur est correcte ou non.
    return True si OK ou False si KO.
    """
    def correction(self, choix_utilisateur):
        if choix_utilisateur == self.reponse:
            return True
        else:
            return False

    """
    Permet de recuperer la reponse d'une question
    """
    def get_reponse(self):
        return self.reponse

    """
    Permet de recuperer les choix d'une question
    """
    def get_choix(self):
        return self.choix

    """
    Permet de recuperer la question
    """
    def get_question(self):
        return self.question

    """
    Permet de shuffle les choix
    """
    def shuffle_choix(self):
        random.shuffle(self.choix)
