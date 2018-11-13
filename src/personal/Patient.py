from .Person import Person
from src.medicine.PrescriptionList import *


class Patient(Person):
    def __init__(self, firstname, lastname, idnumber, room, prescriptionList : PrescriptionList = None):
        super(). __init__(firstname, lastname, idnumber)

        self.position = "Patient"
        self.username = idnumber
        self.room = room
        self.prescriptionList = prescriptionList

    def __str__(self):
        return self.position + " " + super().__str__() + " från rum " + str(self.room)
