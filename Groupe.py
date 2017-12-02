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
        print(self.eleves)
        return len(self.eleves) == 2