from .Menu import Menu
from ..personal.PatientManager import *


class RoomMenu(Menu):
    def __init__(self, patientManager : PatientManager):
        super().__init__("Rumsmeny",
                         "Meny för att komma åt de olika patienterna på boendet",
                         ["Lista alla patienter",
                          "Access till patient"])

        self.patientManager = patientManager
    def action(self):
        while True:
            self.display()
            choise = int(input("Ange ett val: "))
            if choise >= len(self.actions):
                print("Ogiltigt val!")
                choise = -1
            else:
                print("Du valde: " + self.actions[choise])

            if choise is 0:
                return 0
            elif choise is 1:
                self.patientManager.listPatients()
            elif choise is 2:
                while True:
                    room = int(input("Ange vilket rum patienten bor i: "))

                    if self.patientManager.hasPatient(room):
                        patient = self.patientManager.getPatient(room)
                        return patient
                    elif int(room) is 0:
                        return 0
                    else:
                        print("Rum " + str(room) + " finns inte i våran databas!")
