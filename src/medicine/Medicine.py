class Medicine:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "Medicin: " + self.name + "\nBeskrivning: " + self.description
