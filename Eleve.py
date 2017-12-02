class Eleve:
    def __init__(self, nom, prenom, notes):
        self.nom = nom
        self.prenom = prenom
        self.notes = notes

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getNotes(self):
        return self.notes
