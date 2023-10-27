import random

class Question:
    def __init__(self, question, reponses):
        self.question = question
        self.reponses = reponses

    """
    Permet de connaitre si la reponse de l'utilisateur est correcte ou non.
    return True si OK ou False si KO.
    """
    def correction(self, choix_utilisateur):
        for reponse in self.reponses:
            if reponse.get_content() == choix_utilisateur and reponse.is_answer_correct():
                return True
        return False

    """
    Permet de recuperer la bonne reponse d'une question
    """
    def get_reponse_correct(self):
        for reponse in self.reponses:
            if reponse.is_answer_correct():
                return reponse.get_content()
        return None

    """
    Permet de recuperer les reponses d'une question
    """
    def get_reponse(self):
        return [reponse.get_content() for reponse in self.reponses]

    """
    Permet de recuperer l'intitulé de la question
    """
    def get_question(self):
        return self.question

    """
    Permet de shuffle les reponses
    """
    def shuffle_reponses(self):
        random.shuffle(self.reponses)
