from .Staff import Staff


class Caregiver(Staff):
    def __init__(self, firstNmae, lastName, idnumber, pasword):
        super().__init__(firstNmae, lastName, idnumber, pasword)

        self.position = "Vårdare"
