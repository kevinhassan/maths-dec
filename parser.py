import csv
import numpy as np
import sys
from mention import *

'''
	File = String pointant sur le fichier csv de la forme :
		-1,B,AB
		TB,-1,AR
		TB,AB,-1
	Les valeurs du fichier sont :
		Tres bien = TB
		...
		A rejeter = AR
		Diagonale = -1
	Renvoie une liste:
		Premier argument = matrice de preferences
		Second argument = liste des eleves
'''


def parseCSV(file):
    tmp = []
    with open(file) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            tmp.append(','.join(row).split(','))
    matrice = np.array(tmp)
    return matrice[1:matrice.shape[0], 1:matrice.shape[0]], matrice[0][1:matrice.shape[0]]


'''
	Convertie une matrice de la forme :
			[[-1,B,AB]
			 [TB,-1,AR]
			 [TB,AB,-1]]
	En une matrice de la forme :
			[[-1  3  2]
			 [ 4 -1  0]
			 [ 4  2 -1]] 
	Les valeurs sont :
		5 = TB
		...
		0 = AR
		-1 = -1
'''


def convertToInt(matrice):
    res = []
    for x in range(0, np.shape(matrice)[0]):
        tmp = []
        for y in range(0, np.shape(matrice)[0]):
            # Si le dictionnaire contient la mention alors on ajoute la valeur à la matrice des appréciations
            if(matrice[x][y] in mention):
                tmp.append(mention[matrice[x][y]])
            else:
                print("error", matrice[x][y])
        res.append(tmp)
    return np.array(res)


'''
	Ecrit dans un fichier csv pointant sur fichier la matrice repartition de la forme :
		[[1,2],
		 [3,4,5],
		 [6,7],
		 [8,9,10]]
	(Les chiffres representent les eleves)
'''


def writeCsv(file, repartition):
    with open(file, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for x in range(0, len(repartition)):
            repartition[x].insert(0, x + 1)
            spamwriter.writerow(repartition[x])


'''
	Genere une matrice carre aleatoire de taille : size
	Les valeurs sont comprises entre 0 et 4 et la diagonale = -1
'''


def matriceAleatoire(size):
    matrice = np.random.rand(size, size)
    for x in range(0, np.shape(matrice)[0]):
        for y in range(0, np.shape(matrice)[0]):
            if x == y:
                matrice[x][y] = -1
            else:
                matrice[x][y] = (int)(matrice[x][y] * 5)
    return matrice

""""
''' EXEMPLE D'UTILISATION '''
res = parseCSV(sys.argv[1])

matrice = res[0]
listeEleves = res[1]

print("Nombre d'eleves : ", len(listeEleves))
print(listeEleves)
print("Matrice preferences en mention : ")
print(matrice)

eleveX = 12
eleveY = 23

print(listeEleves[eleveX], " -> ", listeEleves[eleveY],
      " = ", matrice[eleveX][eleveY])

print("Matrice preferences en INT : ")
matriceInt = convertToInt(matrice)

print(matriceInt)

print(listeEleves[eleveX], " -> ", listeEleves[eleveY],
      " = ", matriceInt[eleveX][eleveY])

repartition = np.array([[1, 2],
                        [3, 4, 5],
                        [6, 7],
                        [8, 9, 10]])

writeCsv("csv2.csv", repartition)

print("Matrice aleatoire de taille 12 : ")
print(matriceAleatoire(12))"""
