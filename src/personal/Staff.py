from .Person import Person


class Staff(Person):
    def __init__(self, firstName, lastName, idnumber, password):
        super().__init__(firstName, lastName, idnumber)

        self.position = "Personal"
        self.username = idnumber
        self.password = password

    def __str__(self):
        return self.position + " " + super().__str__()
