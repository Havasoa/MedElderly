from .Staff import Staff


class Ssk(Staff):
    def __init__(self, firstName, lastName, idnumber, password):
        super(). __init__(firstName, lastName, idnumber, password)

        self.position = "SSK"
        

