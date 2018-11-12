from .Staff import *
from src.menusystem.Menu import Menu

class Caregiver(Staff):
    def __init__(self, firstNmae, lastName, idnumber, password):
        super().__init__(firstNmae, lastName, idnumber, password)

        self.position = "Vårdare"