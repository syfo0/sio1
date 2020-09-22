from random import *

resultat = randint(1,1000)
print(resultat)
compteur=0
print('Un nombre entre 1 et 1000 est choisi : vous avez 10 essais pour le deviner')
pas_encore_gagne = True

while compteur < 10 and pas_encore_gagne :
    compteur = compteur + 1
    print('Essai n°', compteur)
    n=int(input('Entrer un entier entre 1 et 1000 : '))
    if (n<resultat):
        print(n, ' est trop petit : entrer une valeur plus grande')
    if (n>resultat):
        print(n, ' est trop grand: entrer une valeur plus petite')
    if (n==resultat):
        print(n)
        print('Vous avez gagné au bout de', compteur, 'essais')
        pas_encore_gagne = False

if pas_encore_gagne  :
    print('PERDU')
