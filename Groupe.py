class PresentException(Exception):
    pass

class Groupe: 
    def __init__(self,eleves):
        self.eleves = eleves
    
    def getEleve(self):
        return self.eleves
    
    def supprimerEleve(self,eleve):
        self.eleves.remove(eleve)

    """
        Vérifier l'unicité de l'élève lors de l'ajout
        Vérifier que le groupe n'est pas encore rempli
    """
    def ajouterEleve(self,eleve):
        try:
            if len(self.eleves) > 2:
                raise ValueError("l'année saisie est négative ou nulle")
            elif eleve in self.eleves: 
                raise PresentException("l'année saisie est négative ou nulle")
            else:
                self.eleves.append(eleve)                
        except ValueError:
            print("Erreur : nombre d'élève du groupe dépassé")
        except PresentException:
            print("Erreur : eleve déjà présent dans le groupe")