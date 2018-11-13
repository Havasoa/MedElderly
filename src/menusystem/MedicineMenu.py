from .Menu import Menu
from src.personal.Patient import *


class MedicineMenu(Menu):
    def __init__(self, patient : Patient):
        super().__init__("Medicinlista",
                         patient.__str__(),
                         patient.prescriptionList.prescriptions)