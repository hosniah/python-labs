'''
Exercice 8: Rock Paper Scissors

Faire un jeu à deux joueurs pierre-papier-ciseaux. (Indice : Demandez le joueur
joue (en utilisant les données d’entrée), les compare, imprime un message de félicitations
au vainqueur, et demander si les joueurs veulent commencer un nouveau jeu)

Rappelez-vous les règles :

La pierre bat les ciseaux
Ciseaux bat le papier
Le papier bat la pierre

'''

# Solution
user_one = input("Name of player one:")
user_two = input("Name of player two:")
while True:
    # Input 
    try:
        user_one_answer = int(input("{}, Please input your choice:\n1.Rock\n2.Scissors\n3.Paper\n".format(user_one)))
        user_two_answer = int(input("{}, Please input your choice:\n1.Rock\n2.Scissors\n3.Paper\n".format(user_two)))
        # Check input
        if user_one_answer not in range(1,4) or user_two_answer not in range(1,4):
            print("Input outrange")
            continue
    except:
        print("Input error.")
        continue
    # Compare
    if user_one_answer + 1 == user_two_answer or user_one_answer - 2 == user_two_answer:
        print("{} win!".format(user_one))
    elif user_one_answer == user_two_answer:
        print("Draw.")
    else:
        print("{} win!".format(user_two))
    # Start a new game
    try:
        if int(input("Input number 1 to star a new game, or any to exit.")) == 0:
            break
    except:
        print("Input error. Exit the game.")
        break
    
