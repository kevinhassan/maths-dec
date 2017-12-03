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

    def getMentionSurEleve(self,eleve):
        return self.notes[eleve.getId()]

    """
        Correspond à la satisfaction d'un élève d'être avec d'autres élèves
        Mention minimum donne la satisfaction de l'élève
    """
    def getSatisfaction(self,eleves):
        satisactions = []
        for eleve in eleves: 
            satisactions.append(self.getMentionSurEleve(eleve))
        return min(satisactions)

    def setSatisfaction(self, satisfaction):
        self.satisfaction = satisfaction