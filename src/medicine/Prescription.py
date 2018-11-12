from .Medicine import Medicine


class Prescription:
    def __init__(self, patient, medicine : Medicine, time_to_Take):
        self.patient = patient
        self.medicine = medicine
        self.time_to_Take = time_to_Take

    def __str__(self):
        return "Recept: \n" + self.medicine.__str__() + \
               "\nPatient: " + self.patient.lastName + ", " + self.patient.firstName + \
               "\ntime_to_Take: " + self.time_to_Take
