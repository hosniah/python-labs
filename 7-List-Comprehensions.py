'''
Exercice 7 : Compréhension des listes

Disons que je vous donne une liste sauvegardée dans une variable :
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Écrire une ligne de
Python qui prend cette liste a et fait une nouvelle liste qui a
seuls les éléments pairs de cette liste.

'''

# Solution
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([i for i in a if i % 2 == 0])
