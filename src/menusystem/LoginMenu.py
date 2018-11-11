from .Menu import Menu
from src.usermanager.UserManager import UserManager


class LoginMenu(Menu):
    def __init__(self, userManager : UserManager):
        super().__init__("Login",
                         "Skriv in ditt personnummer:",
                         [])

        self.userManager = userManager

    def action(self):
        self.display()
        idnumber = input()

        if self.userManager.hasUser(idnumber):
            user = self.userManager.getUser(idnumber)

            password = input("Skriv in ditt lösenord:\n")
            if password is user.password:
                print("Vi loggade in som " + user.__str__())

        if int(idnumber) is 0:
            return 0
