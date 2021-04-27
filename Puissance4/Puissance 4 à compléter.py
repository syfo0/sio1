#-------------------------------------------------------------------------------
# Name: PUISSANCE 4      module1 A COMPLETER
# Purpose: Controle du jeu entre deux joueurs



numero=['1','2','3','4','5','6','7']         #stocke les numero des colonnes

plat=[ ['_' for j in range(7)] for i in range(6)]            #stocke le plateau de jeu


compt=0

def affplat():          #Procedure d'affichage
    for i in range(6):
        print(plat[i])
    print()
    print(numero)
    print()


def gagne(i,j):     #Procedure de recherche de partie gagne
    gagneverti=False
    gagnehoriz=False
    jeton=plat[i][j]

    for k in range(4):                          #Recherche la ligne horizontale
        n=0
        while n<4 and plat[i][k+n]==jeton:
            n=n+1
        if n>=4:
            gagnehoriz=True

    if i<3:                                     #Recherche de colonne verticale
        n=1
        while n<4 and plat[i+n][j]==jeton:
            n=n+1
        if n>=4:
            gagneverti=True

    if (gagneverti or gagnehoriz):
        print('Partie finie, les',jeton,'gagnent')

    return(gagneverti or gagnehoriz)


affplat()
print('')

while compt<42:       #CONTROLE DE JEU A COMPLETER ET A MODIFIER DANS LA PARTIE B
    joueur=int(input('Entrez la colonne que vous voulez jouer : '))

    a=compt%2
    ligne = 5
    if a==0:
        plat[ligne][joueur-1]='X'
    else:
        plat[ligne][joueur-1]='O'
    affplat()
    compt=compt+1



if compt>=42:
    print('Partie nulle')
