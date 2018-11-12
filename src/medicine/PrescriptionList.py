from .Prescription import *


class PrescriptionList:
    def __init__(self, patient, prescriptions = []):
        self.patient = patient
        self.prescriptions = prescriptions

    def __str__(self):
        prescriptionStrings = ""
        for prescription in self.prescriptions:
            prescriptionStrings += prescription.__str__() + "\n=========\n"

        return "Receptlista för " + self.patient.__str__() + "\n" + prescriptionStrings

