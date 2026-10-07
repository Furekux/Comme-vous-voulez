import pile
import file
def inverser_chaine(c):
    p=[]
    for i in range(len(c)):
        p.append(list(c).pop(-1-i))
    if type(c) == str :
        mot=""
        for i in range(len(p)):
            mot+=p[i]
        return str(mot)
    return p

def taille(p):
    return len(p)

