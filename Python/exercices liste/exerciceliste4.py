eleves = [["Inès", 14, 12],["Malo", 9, 15],["Léa", 17, 19],["Yanis", 11, 8]]
for i in range(len(eleves)):
    print(eleves[i][0],"a",eleves[i][2],"en NSI")

def moyenne_nsi(t):
    somme=0
    for i in range(len(t)):
        somme+=t[i][2]
    return somme/len(t)

def meilleur_maths(t) :
    max = 0
    for i in range(len(t)):
        if t[i][1]>t[max][1]:
            max = i
    return t[max][0]

def bonus_maths(t, points):
    for i in range(len(t)):
        t[i][1]+=points
        if t[i][1]>20:
            t[i][1]=20

assert moyenne_nsi(eleves) == 13.5
assert meilleur_maths(eleves) == "Léa"
bonus_maths(eleves, 4)
assert eleves[0][1] == 18 and eleves[1][1] == 13
assert eleves[2][1] == 20 and eleves[3][1] == 15