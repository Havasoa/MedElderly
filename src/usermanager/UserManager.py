class UserManager:
    def __init__(self):
        self.users = []

    def appendUser(self, idnumber):
        if self.users.__contains__(idnumber):
            print(idnumber + " finns redan i systemet")
            return False
        else:
            self.users.append(idnumber)
            return True

    def hasUser(self, idnumber):
        return self.users.__contains__(idnumber)

    def removeUser(self, idnumber):
        return self.users.remove(idnumber)
