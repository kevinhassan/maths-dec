import sys
from parser import parseCSV,convertToInt
from Eleve import Eleve

res = parseCSV(sys.argv[1])
preferences = convertToInt(res[0])
eleves = res[1]
eleves = list(map(lambda x: tuple(x.split(" ")), eleves))



for i in range(0,len(eleves)): 
    eleve = eleves[i]
    eleves[i] = Eleve(eleve[1],eleve[0],preferences[i])