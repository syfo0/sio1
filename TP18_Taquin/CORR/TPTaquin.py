# TP Taquin sans interface graphique
from random import randint

taille = 3

tab = [[(1 + i*taille + j)%(taille**2) for j in range(taille)] for i in range(taille)]
ligne_case_vide = taille - 1
colonne_case_vide = taille -1

resolu = [[(1 + i*taille + j)%(taille**2) for j in range(taille)] for i in range(taille)]



def affiche():
    for i in range(taille):
        print(tab[i])


def haut():
    global ligne_case_vide
    if ligne_case_vide>0 :
        tab[ligne_case_vide][colonne_case_vide] = tab[ligne_case_vide-1][colonne_case_vide]
        tab[ligne_case_vide-1][colonne_case_vide] = 0
        ligne_case_vide = ligne_case_vide-1

def bas():
    global ligne_case_vide
    if ligne_case_vide<taille - 1 :
        tab[ligne_case_vide][colonne_case_vide] = tab[ligne_case_vide+1][colonne_case_vide]
        tab[ligne_case_vide+1][colonne_case_vide] = 0
        ligne_case_vide = ligne_case_vide+1

def gauche():
    global colonne_case_vide
    if colonne_case_vide>0 :
        tab[ligne_case_vide][colonne_case_vide] = tab[ligne_case_vide][colonne_case_vide-1]
        tab[ligne_case_vide][colonne_case_vide-1] = 0
        colonne_case_vide = colonne_case_vide-1

def droite():
    global colonne_case_vide
    if colonne_case_vide < taille-1 :
        tab[ligne_case_vide][colonne_case_vide] = tab[ligne_case_vide][colonne_case_vide+1]
        tab[ligne_case_vide][colonne_case_vide+1] = 0
        colonne_case_vide = colonne_case_vide+1


def gameover():
    resu = True
    for i in range(taille):
        for j in range(taille):
            if tab[i][j] != resolu[i][j]:
                resu = False
    return resu

def melange():
    for i in range(taille**4):
        tirage = randint(1,4)
        if tirage == 1:
            haut()
        if tirage == 2:
            bas()
        if tirage == 3:
            gauche()
        if tirage == 4:
            droite()
melange()

