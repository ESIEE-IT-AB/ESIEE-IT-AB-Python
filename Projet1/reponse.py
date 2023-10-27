class Reponse:
    def __init__(self, content, is_correct=False):
        self.content = content
        self.is_correct = is_correct

    def get_content(self):
        return self.content

    def is_answer_correct(self):
        return self.is_correct
