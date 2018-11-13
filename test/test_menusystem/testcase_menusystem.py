import unittest
from unittest import mock

from src.menusystem.RoomMenu import *


choises = (choise for choise in [5, 0, 1])

def mock_input(prompt):
    choise = next(choises)
    print(prompt + str(choise))
    return choise

class testcase_Menusystem(unittest.TestCase):

    def test_ReturnChoise(self):
        print("***************")
        print("TEST RETURN MENU CHOISE")
        print("***************")

        mainMenu = Menu("Huvudmeny",
                        "Detta är ett program för att hålla koll på äldres mediciner.",
                        ["Logga in"])
        mainMenu.actions[0] = "Avsluta"

        ## Vi testar att först skriva fel och sedan skriva rätt
        with mock.patch('builtins.input', mock_input):
            returnChoise = mainMenu.action()
            self.assertEqual(0, returnChoise, "The menu did not go back when we chose 0")

        with mock.patch('builtins.input', mock_input):
            returnChoise = mainMenu.action()
            self.assertEqual(1, returnChoise, "The menu did not go back when we chose 1")

        print("***************")


room_list_choises = (choise for choise in [5, 1, 0])

def mock_list_room_input(prompt):
    room_choise = next(room_list_choises)
    print(prompt + str(room_choise))
    return room_choise

patient_room_choises = (choise for choise in [2, 20, 50, 25, 3, 5, 2, 0])

def mock_patient_room_input(prompt):
    room_choise = next(patient_room_choises)
    print(prompt + str(room_choise))
    return room_choise

class testcase_RoomMenu(unittest.TestCase):
    inge = Patient("Inge", "Olsson", "421101", 5)

    patientManager = PatientManager([inge,
                                     Patient("Claesson", "Inga", "370506", 65)])
    roomMenu = RoomMenu(patientManager)

    def test_ListPatients(self):
        print("***************")
        print("TEST LIST PATIENTS")
        print("***************")

        with mock.patch('builtins.input', mock_list_room_input):
            returnChoise = self.roomMenu.action()
            self.assertEqual(0, returnChoise, "The menu did not go back when we chose 0")

        print("***************")
    def test_GetPatient(self):
        print("***************")
        print("TEST GET PATIENT")
        print("***************")

        with mock.patch('builtins.input', mock_patient_room_input):
            returnPatient = self.roomMenu.action()
            print("Patienten vi fick tillbaka var: " + returnPatient.__str__())
            self.assertEqual(self.inge, returnPatient, "We didn't return the correct patient: " + returnPatient.__str__())

        with mock.patch('builtins.input', mock_patient_room_input):
            returnPatient = self.roomMenu.action()
            print("Returvärdet vi fick tillbaka var: " + returnPatient.__str__())
            self.assertEqual(0, returnPatient, "We didn't return 0: " + returnPatient.__str__())

        print("***************")
if __name__ == '__main__':
    unittest.main()
