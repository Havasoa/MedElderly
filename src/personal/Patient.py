from.Person import Person

class Patient(Person):
    def __init__(self, firstname, lastname, idnumber):
        super(). __init__(firstname, lastname, idnumber)

        self.positione = "Patient"
        self.username = idnumber

    def __str__(self):
        return self.positione + " " + super().__str__()
