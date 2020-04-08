#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Exercice:

Créer un programme qui demande à l’utilisateur d’entrer son nom et son âge. 
Imprimez un message qui leur dit l’année où ils auront 100 ans.

'''


import datetime

while True:
    name = input("Veuillez introduire votre nom：")
    age = int(input("Veuillez introduire votre age："))

    now = datetime.datetime.now()

    this_year = now.year

    print(name + " en " + str(this_year - age + 100) + ", vous aurez 100 ans")
    print()
    in_program = input("Voulez vou continuer？OUI[1], NON[0]：")

    if in_program == '0':
        break
