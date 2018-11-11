from .Menu import Menu


class LoginMenu(Menu):
    def __init__(self, userManager):
        super().__init__("Login",
                         "Skriv in ditt personnummer:",
                         [])

        self.userManager = userManager

    def action(self):
        # Här ska vi skriva vår login procedur.

        idnumber = input()

        if self.userManager:
            print("Checka personnumer")
