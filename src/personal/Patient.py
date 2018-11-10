from.Person import Person

class Patient(Person):
    def __init__(self, firstname, lastname, idnumber):
        super(). __init__(firstname, lastname, idnumber)

        self.position = "Patient"
        self.username = idnumber

    def __str__(self):
        return self.position + " " + super().__str__()
