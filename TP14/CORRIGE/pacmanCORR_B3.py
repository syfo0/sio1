8# CCF PacMan

# définition de la variable plateau
plateau = [ [2 for j in range(7) ] for i in range(7)]

for k in range(1,6):
    plateau[0][k] = -1
    plateau[6][k] = -1

for k in range(7):
    plateau[k][6] = -1
    plateau[k][0] = -1

plateau [3][4] = -1

lin = 2
col = 3
plateau [lin][col] = 7


# définition de la variable tab1
tab1 = [[-1, -1, -1, -1, -1, -1, -1],
        [-1,  2,  2,  2,  2,  2, -1],
        [-1,  0,  0,  0,  2,  2, -1],
        [-1,  0,  7,  2, -1,  2, -1],
        [-1,  0,  0,  2,  2,  2, -1],
        [-1,  0,  0,  2,  2,  2, -1],
        [-1, -1, -1, -1, -1, -1, -1]]

# on initialise la variable score
score = 0
# cette variable sera modifiée dans 2 cas
# 1. on appuie sur une touche : elle est décrémentée de 1
# 2. on se déplace sur une pac-gomme : elle est incrémentée de +2
# ==> voir la fonction deplacement


def convert_ligne(tab, i):
        ligne = ''
        for j in range(7):
            case = tab[i][j]
            if case == 2:
                ligne = ligne + '..'
            if case == -1:
                ligne = ligne + 'XX'
            if case == 0:
                ligne = ligne + '  '
            if case == 7:
                ligne = ligne + '[]'

        return ligne

def affichage() :
    for i in range(7):
        print(convert_ligne(plateau,i))
    print()
    print ('SCORE =' , score)
    print()


def nb_cases(tab, n):
    resu = 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == n:
                resu = resu+1
    return resu

def deplacement(touche) : # touche est un caractère saisi sur le pavé numérique pour indiquer un mouvement
# 8 : vers le haut
# 4 : vers la gauche
# 6 : vers la droite
# 2 : vers le bas
    global lin, col, plateau, score
    print(' * * *')
#### on commence par modifier la variable score, à cause d'un appui sur une des touches
    score = score -1
    if touche == '8' : # mouvement vers le haut
        if plateau[lin-1][col] != -1 :
            print ('monter')
            plateau [lin][col] = 0
            lin = lin - 1
            # si la nouvelle case est une pac-gomme, le score augmente de deux points
            if plateau[lin][col] == 2:
                score = score + 2
            plateau [lin][col] = 7

    if touche == '2' : # mouvement vers le bas
        if plateau[lin+1][col] != -1 :
            print ('descendre')
            plateau [lin][col] = 0
            lin = lin + 1
            # si la nouvelle case est une pac-gomme, le score augmente de deux points
            if plateau[lin][col] == 2:
                score = score + 2
            plateau [lin][col] = 7


    if touche == '6' : # mouvement vers la droite
        if plateau[lin][col+1] != -1 :
            print ('droite')
            plateau [lin][col] = 0
            col = col + 1
            # si la nouvelle case est une pac-gomme, le score augmente de deux points
            if plateau[lin][col] == 2:
                score = score + 2
            plateau [lin][col] = 7

    if touche == '4' : # mouvement vers la gauche
        if plateau[lin][col-1] != -1 :
            print ('gauche')
            plateau [lin][col] = 0
            col = col - 1
            # si la nouvelle case est une pac-gomme, le score augmente de deux points
            if plateau[lin][col] == 2:
                score = score + 2
            plateau [lin][col] = 7




while nb_cases(plateau,2)>0:
    touche = input("quelle direction ?")
    deplacement (touche)
    affichage()
print ('fin de partie')

