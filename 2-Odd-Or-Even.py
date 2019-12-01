'''
Exercice 2 : Impair ou pair

Demandez à l’utilisateur un nombre. Selon que le nombre est pair ou impair,
imprimer un message approprié à l’utilisateur. Astuce : comment faire un pair / impair
le nombre réagit différemment lorsqu’il est divisé par 2?

Extras :
Si le nombre est un multiple de 4, imprimez un message différent.
Demandez à l’utilisateur pour deux numéros : un numéro à vérifier (appelez-le num) et un nombre à diviser par (check). 
Si le check se divise également en nombre, indiquez que à l’utilisateur. Sinon, imprimez un message différent approprié.
'''

input_number = int(input('Please input a number (num):'))
input_check = int(input('Please input a check number (check):'))

result_message = "Your input is an even number." if input_number % 2 == 0 else "Your input is an odd number."
result_message += "\nYour input is a multiple of 4." if input_number % 4 == 0 else ""
number_divided = "divides" if input_number % input_check == 0 else "dose not divide"
result_message += "\nYour input number {yes_or_not} evenly by {check}".format(yes_or_not = number_divided, check = input_check)
print(result_message)
