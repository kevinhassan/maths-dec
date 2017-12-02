import sys
from parser import convertToInt, parseCSV

from Eleve import Eleve
from Groupe import Groupe

"""
    Récupérer la matrice de préférence
    Récupérer le nom des élèves 
"""
res = parseCSV(sys.argv[1])
preferences = convertToInt(res[0])
eleves = res[1]
eleves = list(map(lambda x: tuple(x.split(" ")), eleves))

"""
    Calculer le nombre de Binome Trinome à créer
"""
nbEleve = len(eleves)
nbBinome = nbEleve // 2
if(nbEleve - nbBinome * 2 == 1):
    nbBinome = nbBinome - 1

nbTrinome = (nbEleve - nbBinome * 2)//3

"""
    Créer les élèves grâce aux données associées
    Ajout dans une liste d'élèves : eleves
"""
for i in range(0, len(eleves)):
    eleve = eleves[i]
    eleves[i] = Eleve(i,eleve[1], eleve[0], preferences[i])

""" 
    Associer les élèves entre eux dans des binomes et/ou trinomes
"""
binomes = []
binome = []

#Former les binomes
for i in range(0, nbBinome*2): 
    binome.append(eleves[i])
    if i%2 != 0 :
        #ajouter le binome constitué et l'effacer 
        binomes.append(binome)
        binome = [eleves[i]]
    

trinomes = []
trinome = []

#Former les trinomes
for i in range(nbBinome*2, nbBinome*2 + nbTrinome*3): 
    trinome.append(eleves[i])
    if i>nbBinome*2 and i%2 == 0 :
        #ajouter le binome constitué et l'effacer 
        trinomes.append(trinome)
        trinome = [eleves[i]]