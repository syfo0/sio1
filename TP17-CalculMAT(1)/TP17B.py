def somme(M,N):
    nblignes = len(M)
    nbcolonnes = len(M[0])
    assert len(N) == len(M) and len(N[0]) == len(M[0])
    resu=[ [0 for j in range (nbcolonnes)] for i in range (nblignes)]

    for i in range(nblignes):
        for j in range(nbcolonnes):
            resu[i][j] = M[i][j] + N[i][j]
    return resu

def nombre_fois_tableau(k,M):
    nblignes = len(M)
    nbcolonnes = len(M[0])
    resu=[ [0 for j in range (nbcolonnes)] for i in range (nblignes)]

    for i in range(nblignes):
    # pour chaque indice de ligne
        for j in range(nbcolonnes):
        # pour chaque indice de colonne
            resu[i][j] = k * M[i][j]
    return resu

def difference(M,N):
    oppN = nombre_fois_tableau(-1,N)
    return somme(M, oppN)

A =[[1,2,3],
    [4,5,6],
    [7,8,9]]

B =[[1,4,7],
    [2,5,8],
    [3,6,9]]

C =[[0,-4,70],
    [20,15,88],
    [-3,76,19]]

D = [[1,2,3],
     [4,5,6]]

E =[[0,-4,70],
    [20,15,88]]


