from random import *
from time import *


def nb_mystere() :
    nombre = randint(1,1000)
    test = 0
    while test != nombre :
        test = 0
        while test < 1 or test > 9999 :
            test = int(input("choisissez un nombre entre 1 et 9999 : "))
        if test < nombre :
            print("plus grand")
        elif test > nombre :
            print("plus petit")
    print("vous avez gagné le nombre était",nombre)
    sleep(2)

def trouver_nb() :
    print("choisissez un nombre entre 1 et 9999 et retenez le")
    bmin=0
    bmax=10000
    while True :
        test = (bmax-bmin)//2 + bmin
        print(test)
        rep=input("+ ou - ou = : ")
        if rep == "=" :
            print("j'ai gagné")
            break
        elif rep == "+" :
            bmin = test+1
        else :
            bmax = test-1

    
while True :
    print("1 : deviner le chiffre de la machine")
    print("2 : la machine devine votre nombre")
    print("3 : quitter")
    choix=input("votre choix :")
    if choix == "2" :
        trouver_nb()
    elif choix == "1" :
        nb_mystere()
    elif choix == "3" :
        break

