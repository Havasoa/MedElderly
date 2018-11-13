import unittest
from unittest import mock

from src import MedElderly_Main

choises = (choise for choise in [5, 1, # Huvudmeny
                                 "880815", "2220", "2320", # Login
                                 1, # Personalmeny
                                 1, 2, # Patientmeny
                                 55, 666, # Rumsmeny
                                 60, 1, # Medicinmeny
                                 0 # Avslut
                                 ])

def mock_input(prompt):
    choise = next(choises)
    print(prompt + str(choise))
    return choise

class testcase_MedElderly(unittest.TestCase):
    def test_program(self):
        print("***************")
        print("TEST OF MEDELDERLY")
        print("***************")

        with self.assertRaises(SystemExit) as cm:
            with mock.patch('builtins.input', mock_input):
                MedElderly_Main.main()

        self.assertEqual(cm.exception.code, 0)
        print("Medeldely har körts och funkar!")

        print("***************")


if __name__ == '__main__':
    unittest.main()