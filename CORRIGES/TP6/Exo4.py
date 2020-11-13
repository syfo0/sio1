from turtle import *

n = int(input("entrer le nombre de côtés  : "))
p = int(input("entrer le nombre de saut  : "))
largeur = 200
for i in range(n):
    forward(largeur)
    left(p*360/n)



