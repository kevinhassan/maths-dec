class Eleve:
    def __init__(self, id, nom, prenom, notes):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.notes = notes

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getNotes(self):
        return self.notes
    
    def getId(self):
        return self.id

    def getSatisfactionSurEleve(self,eleve):
        return self.notes[eleve.getId()]