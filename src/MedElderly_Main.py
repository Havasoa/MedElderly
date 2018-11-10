from src.menusystem.Menu import Menu


def main():
    mainMenu = Menu("Huvudmeny",
                    "Detta är ett program för att hålla koll på äldres mediciner.",
                    "Var god skriv in Personnummer",
                    ["Logga in"])
    mainMenu.actions[0] = "Avsluta"

    runningProgram = True

    while runningProgram:
        choise = mainMenu.action()

        if choise is 0:
            print("Tack för att du valde MedElderly")
            exit(0)
        else:
            print("Du valde att gå vidare men detta är inte implementerat än!")

if __name__ == "__main__":
    main()
