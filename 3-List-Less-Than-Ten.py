'''
Exercice 3 : Liste de moins de dix
Prenez une liste, par exemple celle-ci :

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

et écrivez un programme qui imprime tous les éléments de la liste qui sont inférieurs à 5.

Extras:
1. Au lieu d’imprimer les éléments un par un, faites une nouvelle liste qui contient tous les éléments
moins de 5 de cette liste et imprimer cette nouvelle liste.
2. Écrivez ceci dans une ligne de Python.
3. Demandez à l’utilisateur un numéro et renvoyez une liste qui ne contient que des éléments du
liste originale a qui sont plus petits que le nombre donné par l’utilisateur.
'''

input_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Solution
print("Solution")

for i in input_list:
    if i < 5:
        print(i)
        
# Extras
print("Extras")

cut_off = int(input("Please input the cut off number:"))
new_list = [i for i in input_list if i < cut_off]
print(new_list)
