import sys
from parser import convertToInt, parseCSV

from Eleve import Eleve

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
    eleves[i] = Eleve(eleve[1], eleve[0], preferences[i])