class Question:
    def __init__(self, question, choix1, choix2, choix3, reponse):
        self.question = question
        self.choix1 = choix1
        self.choix2 = choix2
        self.choix3 = choix3
        self.reponse = reponse

    """
    Permet de connaitre si la reponse de l'utilisateur est correcte ou non.
    return True si OK ou False si KO.
    """
    def correction(self, choix_utilisateur):
        choix_utilisateur = choix_utilisateur.upper()
        if choix_utilisateur == self.reponse:
            return True
        else:
            return False

    """
    Permet de print la question
    """
    def print_question(self):
        print(self.question)

    """
    Permet de print les 3 choix d'une question
    """
    def print_choix(self):
        print("A : " + self.choix1)
        print("B : " + self.choix2)
        print("C : " + self.choix3)

    """
    Permet de recuperer la reponse d'une question
    """
    def get_reponse(self):
        return self.reponse