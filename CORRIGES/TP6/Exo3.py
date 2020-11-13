from turtle import *

n = int(input("entrer le nombre de côtés  : "))

largeur = 50
for i in range(n):
    forward(largeur)
    left(360/n)



