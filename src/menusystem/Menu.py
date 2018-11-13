class Menu:
    def __init__(self, title : str, description : str = None, actions = []):
        self.title = title
        self.description = description
        self.actions = ["Gå tillbaka"]

        for action in actions:
            self.actions.append(action)

    def display(self):
        print(f"*** {self.title} ***")
        print(f"* {self.description} *")

        for x in range(0, len(self.actions)):
            print(str(x) + ". " + self.actions[x].__str__())

    def action(self):
        choise = -1
        while choise < 0:
            self.display()
            choise = int(input("Ange ett val: "))
            if choise >= len(self.actions):
                print("Ogiltigt val!")
                choise = -1
            else:
                print("Du valde: " + self.actions[choise].__str__())

        return choise
