'''
Exercice 15 : Ordre des mots inversés
Écrire un programme (en utilisant des fonctions!) qui demande à l’utilisateur pour
longue chaîne contenant plusieurs mots. Imprimer à nouveau à la
utilisateur la même chaîne, sauf avec les mots à l’envers
order. Par exemple, disons que je tape la chaîne:

Mon nom est Michele

Puis je voyais la chaîne :

Michele est nom Mon

M'est affiché.

'''

# Solution
def reverse_word(string):
    """
    Reverse the input string.
    
    Arguments:
    string -- a list of input string.
    
    Returns:
    reverse_string -- a string reverse word of input string.
    """
    return ' '.join(string.split(' ')[::-1])
    
# Test Part
print(reverse_word(input('Please input a sentence:')))
