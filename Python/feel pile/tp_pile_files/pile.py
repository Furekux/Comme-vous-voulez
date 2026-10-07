def créer_pile_vide():
    return []
def est_vide(p):
    return p==[]
def empiler(p,x):
    p.append(x)
def depiler(p,x):
    return p.pop(x)
def sommet(p):
    return p[-1]