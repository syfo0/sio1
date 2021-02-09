# CCF PacMan

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


def convert_ligne(tab, i):
        ligne = ''
        for j in range(7):
            case = tab[i][j]
            if case == 2:       # pac-gommme
                ligne = ligne + '..'
            if case == -1:      # obstacle
                ligne = ligne + 'XX'
            if case == 0:       # case vide
                ligne = ligne + '  '
            if case == 7:       # pacman
                ligne = ligne + '<<'

        return ligne

def affichage() :
    for i in range(7):
        print(convert_ligne(plateau,i))
    print()



def deplacement(touche) : # touche est un caractère saisi sur le pavé numérique pour indiquer un mouvement
# 8 : vers le haut
# 4 : vers la gauche
# 6 : vers la droite
# 2 : vers le bas
    global lin, col, plateau, score
    print('DEPLACEMENT')
    if touche == '8' : # mouvement vers le haut
        if plateau[lin-1][col] != -1 :
            print ('monter')
            plateau [lin][col] = 0
            lin = lin - 1
            plateau [lin][col] = 7

    if touche == '2' : # mouvement vers le bas
        if plateau[lin+1][col] != -1 :
            print ('descendre')
            plateau [lin][col] = 0
            lin = lin + 1
            plateau [lin][col] = 7


    if touche == '6' : # mouvement vers la droite
        if plateau[lin][col+1] != -1 :
            print ('droite')
            plateau [lin][col] = 0
            # INSTRUCTION A AJOUTER  ####################

            plateau [lin][col] = 7

    if touche == '4' : # mouvement vers la gauche
        if plateau[lin][col-1] != -1 :
            print ('gauche')
            plateau [lin][col] = 0
            # INSTRUCTION A AJOUTER  ####################

            plateau [lin][col] = 7


def jeu():
    affichage()
    for i in range(25):
        touche = input("quelle direction ?")
        deplacement (touche)
        affichage()
    print ('fin de partie')


# ######################
# progamme principal    A MODIFIER ET COMPLETER
# ######################

jeu()