from.Person import Person

class Patient(Person):
    def __init__(self, firstname, lastname, idnumber, room):
        super(). __init__(firstname, lastname, idnumber)

        self.position = "Patient"
        self.username = idnumber
        self.room = room

    def __str__(self):
        return self.position + " " + super().__str__() + " från rum " + str(self.room)
