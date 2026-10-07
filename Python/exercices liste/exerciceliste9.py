terrain = [[0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
           [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
           [1, 1, 0, 0, 1, 1, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]]

#les 8 voisines de terrain[1][1] sont 00 01 02 10 12 20 21 22
def mines_voisines(t, i, j):
    nb_mines=0-t[i][j]
    for k in range(3):
        for l in range(3):
            if i-1+k>=0 and j-1+l>=0 and i-1+k<len(t) and j+l-1<len(t[i]):
                nb_mines+=t[i-1+k][j-1+l]
    return nb_mines

def carte(t):
    plan=[[0, 0, 0, 0,0,0,0,0,0,0],[0,0,0,0,0,0,0, 0, 0, 0],[0,0,0,0,0,0,0, 0, 0, 0],[0,0,0,0,0,0,0, 0, 0, 0]]
    for k in range(len(t)):
            for l in range(len(t[k])):
                if t[k][l]==1:
                    plan[k][l]=-1
                else :
                    plan[k][l]=mines_voisines(t, k, l)
    return plan


print(carte(terrain))



