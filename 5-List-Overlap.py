'''
Exercice 5 : chevauchement de listes 

Prenez deux listes, par exemple :

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

et écrivez un programme qui retourne une liste qui ne contient que les éléments
qui sont communs entre les listes (sans doublons). Assurez-vous que votre
programme fonctionne sur deux listes de tailles différentes.

Extras :

Générez aléatoirement deux listes pour tester 
Écrivez ceci dans une ligne de Python (ne vous inquiétez pas si vous ne pouvez pas le comprendre
à ce stade - nous y arriverons bientôt)

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
