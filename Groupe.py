class PresentException(Exception):
    pass

class Groupe: 
    def __init__(self,eleves):
        self.eleves = eleves
    
    def getEleve(self):
        return self.eleves
    
    """
        Vérifier que le nombre d'étudiant est supérieur à 0 avant de supprimer
    """
    def supprimerEleve(self,eleve):
        try:
            if eleve in self.eleves: 
                self.eleves.remove(eleve)
            else: 
                raise PresentException("Erreur : élève absent dans le groupe")
        except PresentException as err:
            print(err)

    """
        Vérifier l'unicité de l'élève lors de l'ajout
        Vérifier que le groupe n'est pas encore rempli
    """
    def ajouterEleve(self,eleve):
        try:
            if len(self.eleves) > 2:
                raise ValueError("Erreur : nombre d'élève du groupe dépassé" )
            elif eleve in self.eleves: 
                raise PresentException("Erreur : élève déjà présent dans le groupe")
            else:
                self.eleves.append(eleve)                
        except ValueError as err:
            print(err)
        except PresentException as err:
            print(err)

    def estBinome(self):
        return len(self.eleves) == 2
    
    """
        La note d'une groupe correspond à la mention minimum d'un eleve d'être dans ce groupe
    """
    def getNote(self):
        #Parcourir les élèves du groupe 
        #Récupérer la satisfaction de chacun d'être dans le groupe 
        #Prendre les satisfactions de chaque élève du groupe 
        tmp = self.eleves.copy()
        satisfactions = []
        for eleve in self.eleves:
            tmp.remove(eleve) #supprimer l'élève actuel
            #calculer la satisfaction d'être avec les autres
            satisfactions.append(eleve.getSatisfaction(tmp))
            #on remet tous les élèves dans la liste
            tmp = self.eleves.copy()
        return satisfactions
    
    """
        Récupérer l'élève qui a mis la note la plus faible 
        Principe : regarder les notes données prendre la plus faible 
        et récupérer dans la liste des élèves la position de l'élève dont la note est la plus basse 
    """
    def getMoinsSatisfait(self):
        notes = self.getNote()
        posMin = 0
        for x in range(1,len(notes)):
            if(notes[x]< notes[posMin]):
                posMin = x
        return self.getEleve()[posMin] 

    """
        Comparer 2 groupes entre eux de même satisfaction
    """
    def estPlusGrand(self, g):
        return sum(self.getNote()) > sum(g.getNote())