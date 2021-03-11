#TP13 Tableaux 2 dim

T =[[1,2,3],
    [4,5,6],
    [7,8,9]]


C=[[-1],
    [4],
    [2]]

L = [[5, 9, -2]]

def affiche_tableau(M):
    for i in range(len(M)):
        print (M[i])



def nombre_fois_tableau(k,M):
    nblignes = 3
    nbcolonnes = 3
    resu=[ [0 for j in range (nbcolonnes)] for i in range (nblignes)]

    for i in range(nblignes):
    # pour chaque indice de ligne
        for j in range(nbcolonnes):
        # pour chaque indice de colonne
            resu[i][j] = k * M[i][j]
    return resu
##
##print('Tableau T : ')
##affiche_tableau(T)
##print()
##print('Tableau C : ')
##affiche_tableau(C)
##print()
##print('Tableau L : ')
##affiche_tableau(L)
##print()
##
##print('3 * Tableau T : ')
##affiche_tableau(nombre_fois_tableau(3,T))
##print()
##
##
