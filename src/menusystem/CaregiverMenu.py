from .Menu import Menu

class CaregiverMenu(Menu):
    def __init__(self, caregiver):
        super().__init__("Vårdarmeny",
                         "Vad vill du göra " + caregiver.__str__() + "?",
                         ["Behandla Patient"])