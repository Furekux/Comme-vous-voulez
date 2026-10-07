alphabet = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
# dico de l'alphabet


def recherche_dichotomique(carnet, nom):                                # carnet est une liste de tuples et nom est les nom qu'on cherche
    test = len(carnet)//2                                               # test est ma variable qui bouge pour tester les possibilités donc la avec la formule je l'initialise a la moitié de la liste
    empreinte = 0
    bmin = 0                                                            # bmin c'est ma borne minimale donc je l'initialise a 0
    bmax = len(carnet)                                                  # bmin c'est ma borne minimale donc je l'initialise a la longueur de carnet
    while carnet[test][0] != nom :                                      # boucle tant que j'ai pas trouvé le bon tuple
        i=0                                                             # juste une variable random pour faire un compteur
        a=0
        while carnet[test][0][i] == nom[i]:                             # je regarde la lettre suivante tant que la lettre regardée est identique (par exemple comparer bonjour et bonsoir ça va skip a la 4eme lettre)
            i+=1                                                        # ducoup on monte le compteur pour passer a la lettre suivante
            if i==len(nom) and i!=len(carnet[test][0]):
                a=2
                i-=1
                break
            elif i!=len(nom) and i==len(carnet[test][0]):
                a=1
                i-=1
                break
            elif i==len(nom) and i==len(carnet[test][0]):
                break
        if a==1 or alphabet[carnet[test][0][i]] > alphabet[nom[i]] :            # comparaison si le mot cherché est avant le mot test
            bmax=test                                                           # change la borne max en l'id du test  car on sait que le mot cherché n'est pas après
        elif a==2 or alphabet[carnet[test][0][i]] < alphabet[nom[i]] :          # comparaison si le mot cherché est après le mot test
            bmin=test                                                           # change la borne min en l'id du test  car on sait que le mot cherché n'est pas avant
        test = (bmax-bmin)//2+bmin                                                  # le test prend la valeur au milieu entre les deux bornes

        if test == empreinte :
            return None
        empreinte=test
    return carnet[test]                                                         # on retourne le tuple trouvé



