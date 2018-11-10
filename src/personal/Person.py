class Person:
    def __init__(self, firstName, lastName, idnumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idnumber = idnumber

    def __str__(self):
        return self.firstName + " " + self.lastName

