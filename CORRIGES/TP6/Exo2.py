from turtle import *

n = int(input("entrer le nombre de côtés  : "))

largeur = 20
for i in range(n):
    forward(largeur)
    left(90)
    largeur = largeur + 20



