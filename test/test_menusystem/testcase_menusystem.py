import unittest
from unittest import mock
from src.menusystem.Menu import Menu


choises = (choise for choise in [0, 1])

def mock_input():
    return next(choises)

class testcase_Menusystem(unittest.TestCase):

    def test_GoBack(self):
        mainMenu = Menu("Huvudmeny",
                        "Detta är ett program för att hålla koll på äldres mediciner.",
                        "Var god skriv in Personnummer",
                        ["Logga in"])
        mainMenu.actions[0] = "Avsluta"

        with mock.patch('builtins.input', return_value=mock_input()):
            returnChoise = mainMenu.action()
            self.assertEqual(0, returnChoise, "The menu did not go back when we chose 0")

        with mock.patch('builtins.input', return_value=mock_input()):
            returnChoise = mainMenu.action()
            self.assertEqual(1, returnChoise, "The menu did not go continue when we chose 1")


if __name__ == '__main__':
    unittest.main()