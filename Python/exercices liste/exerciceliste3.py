g = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
g[0][-1]=7
g[-1][0]=3
for i in range(len(g)) :
    g[i][i] = 1
for j in range(len(g)) :
    g[2][j] = 5
for i in range(len(g)) : 
    print(g[i])
assert g == [[1, 0, 0, 7],
             [0, 1, 0, 0],
             [5, 5, 5, 5],
             [3, 0, 0, 1]]