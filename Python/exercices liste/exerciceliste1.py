t = [[3, 8, 1],[7, 2, 9],[4, 6, 5]]
a = t[1][2]
b = t[2][0]
c = t[1][1]
d = t[-1][-1]
nb_lignes = len(t)
nb_colonnes = len(t[0])
ligne = t[1] 
#print(t[3][0]) index out of range parce que le dernier index c'est 2
assert a == 9 and b == 4 and c == 2 and d == 5
assert nb_lignes == 3 and nb_colonnes == 3
assert ligne == [7, 2, 9]