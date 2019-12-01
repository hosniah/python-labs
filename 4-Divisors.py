'''
Exercice 4 : Diviseurs

Créer un programme qui demande à l’utilisateur un numéro, puis imprime
une liste de tous les diviseurs de ce nombre. (Si vous ne savez pas ce que
diviseur est, c’est un nombre qui se divise également en un autre nombre.
Par exemple, 13 est un diviseur de 26 parce que 26 / 13 n’a pas de reste. )

'''

# Solution
number = int(input("Please input a number:"))
divisors = [i for i in range(1, number+1) if number % i == 0]

print("Divisor(s):")
print(divisors)
