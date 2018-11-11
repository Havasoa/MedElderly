from src.personal.Staff import Staff


class UserManager:
    def __init__(self):
        self.users = []

    def appendUser(self, staff : Staff):
        if self.users.__contains__(staff):
            print(staff.idnumber + " finns redan i systemet")
            return False
        else:
            self.users.append(staff)
            return True

    def hasUser(self, idnumber):
        for person in self.users:
            if person.idnumber == idnumber:
                return True

        return False

    def removeUser(self, idnumber):
        return self.users.remove(idnumber)

    def getUser(self, idnumber):
        for person in self.users:
            if person.idnumber == idnumber:
                return person
