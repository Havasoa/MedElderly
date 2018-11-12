from .Patient import *


class PatientManager:
    def __init__(self, patients = []):
        self.patients = patients

    def hasPatient(self, room):
        for patient in self.patients:
            if patient.room == room:
                return True

        return False

    def listPatients(self):
        print("*****************")
        print("Lista på patienter")
        print("*****************")
        for patient in self.patients:
            print("RUM " + str(patient.room) + ": " + patient.lastName + ", " + patient.firstName + " - " + patient.idnumber)
            print("==========")
        print("*****************")

    def getPatient(self, room):
        for patient in self.patients:
            if patient.room == room:
                return patient

        print("Det bor ingen i rumsnummer: " + str(room))

    def addPatient(self, p_patient : Patient):
        for patient in self.patients:
            if patient.room == p_patient.room:
                return False

        self.patients.append(p_patient)
        return True

    def removePatient(self, room):
        for patient in self.patients:
            if patient.room == room:
                self.patients.remove(patient)
                return True

        print("Kunde inte ta bort patient för att det bor ingen i rumsnummer: " + str(room))
        return False
