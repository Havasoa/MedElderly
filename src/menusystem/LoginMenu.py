from .Menu import Menu
from src.usermanager.UserManager import UserManager


class LoginMenu(Menu):
    def __init__(self, userManager : UserManager):
        super().__init__("Login",
                         "Skriv in ditt personnummer",
                         [])

        self.userManager = userManager

    def action(self):
        self.display()

        userExist = False
        while userExist is False:
            idnumber = input("Personnummer: ")

            if int(idnumber) is 0:
                return 0

            if self.userManager.hasUser(idnumber):
                user = self.userManager.getUser(idnumber)

                correctPassword = False
                passwordTriesLeft = 5

                while passwordTriesLeft > 0 or correctPassword is False:
                    password = input("Välkommen " + user.__str__() + "\nSkriv in ditt lösenord:\n")
                    if password == user.password:
                        print("Vi loggade in som " + user.__str__())
                        return user

                    elif(passwordTriesLeft != 0 and not correctPassword):
                        print("Du skrev fel lösenord!")

                        passwordTriesLeft -= 1
                        print("Du har " + str(passwordTriesLeft) + " antal försök kvar")

                    else:
                        print("Du har svarat fel för många gånger!")
                        return 0
            else:
                print("Användare " + idnumber + " finns inte i våran databas!")