from src.menusystem.LoginMenu import LoginMenu
from src.usermanager.UserManager import UserManager
from src.personal.Caregiver import *

from src.medicine.PrescriptionList import *
from src.medicine.Medicine import *
from src.personal.Patient import *

mainMenu = Menu("Huvudmeny",
                "Detta är ett program för att hålla koll på äldres mediciner.",
                ["Logga in"])
mainMenu.actions[0] = "Avsluta"

userManager = UserManager()
loginMenu = LoginMenu(userManager)
careGiver = Caregiver("Marie-Claire", "Carlsson", "880815", "2320")


def main():
    userManager.appendUser(careGiver)

    runningProgram = True

    while runningProgram:
        choise = mainMenu.action()

        if choise is 0:
            print("Tack för att du valde MedElderly")
            exit(0)
        else:
            user = loginMenu.action()

            if user:
                choise = user.menu.action()

                if choise is TREAT_PATIENT:
                    print("Vi har nu kommit till rumsmenyn som ska implementeras!")


if __name__ == "__main__":
    #main()

    patient = Patient("Erik", "Benktsson", "1234567")
    mango = Medicine("Mango", "Är gott för hjärtat")
    insulin = Medicine("Insulin", "För socker halten")
    prescription = Prescription(patient, mango, "10:00")
    prescription2 = Prescription(patient, insulin, "12:00")
    list = PrescriptionList(patient, [prescription, prescription2])

    print(list.__str__())