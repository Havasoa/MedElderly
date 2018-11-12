from .Person import Person
from src.menusystem.Menu import Menu

TREAT_PATIENT = 1

class Staff(Person):
    def __init__(self, firstName, lastName, idnumber, password):
        super().__init__(firstName, lastName, idnumber)

        self.position = "Personal"
        self.username = idnumber
        self.password = password

        self.menu = Menu(self.position + " meny",
                         self.__str__(),
                         ["Behandla patient"])

    def __str__(self):
        return self.position + " " + super().__str__()
