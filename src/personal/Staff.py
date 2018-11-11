from .Person import Person
from src.menusystem.Menu import Menu


class Staff(Person):
    def __init__(self, firstName, lastName, idnumber, password):
        super().__init__(firstName, lastName, idnumber)

        self.position = "Personal"
        self.username = idnumber
        self.password = password

        self.menu = Menu("Personalmeny",
                         self.__str__())

    def __str__(self):
        return self.position + " " + super().__str__()
