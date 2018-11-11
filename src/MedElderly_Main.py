from src.menusystem.Menu import Menu
from src.menusystem.LoginMenu import LoginMenu
from src.usermanager.UserManager import UserManager
from src.personal.Caregiver import Caregiver


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
            loginMenu.action()


if __name__ == "__main__":
    main()
