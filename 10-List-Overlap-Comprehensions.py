'''
Exercice 10 : Compréhension des chevauchements de listes

L’exercice de cette semaine va revenir sur un ancien exercice (voir l’exercice 5). 
Et cette solution est une copie de l’exercice 5.

Extras :

Générez aléatoirement deux listes pour tester

'''
import random
# Solution
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = [int(10 * random.random()) for i in range(20)]
b = [int(10 * random.random()) for i in range(15)]
print("List 1: ", a)
print("List 2: ", b)
print("Overlap: ", list(set(a).intersection(b)))
