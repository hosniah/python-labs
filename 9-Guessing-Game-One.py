'''
Exercice 9 : Première partie de devinette
Générez un nombre aléatoire entre 1 et 9 (y compris 1 et 9). Demandez à l’utilisateur de deviner le
nombre, puis leur dire s’ils ont deviné trop bas, trop élevé, ou exactement droite. (Indice:
n’oubliez pas d’utiliser les leçons d’entrée de l’utilisateur du tout premier exercice)

Extras :

Maintenir le jeu jusqu’à ce que l’utilisateur tape « exit »
Gardez une trace du nombre de devinettes que l’utilisateur a prises, et quand le jeu se termine, imprimez-le.

'''

# Solution
import random

guess_log = []
generated_number = random.randint(1, 9)
while True:
    # Get input
    input_string = input('Guess a number between 1 and 9. Type "exit" to exit the game:')
    if input_string.lower() == 'exit':
        print('See you next time!')
        break
    # Check the input value
    try:
        guess_number = int(input_string)
        if guess_number not in range(1, 10):
            print('Your number is outrange.')
            continue
    except:
        print('Input error.')
        continue
    # Compare
    guess_log.append(guess_number)
    if guess_number != generated_number:
        print('Your guess is too high!' if guess_number > generated_number else 'Your guess is too low!')
    else:
        print('Exactly right! After {} guess(es).\n{}'.format(len(guess_log), guess_log))
        # Reset
        guess_log = []
        generated_number = random.randint(1, 9)
