# parcours d'une chaîne avec saut

chaine = 'ABCDE'
long = len (chaine)
saut = 2
indice = 0
resu = ''

for i in range(long):
    resu = resu + chaine[indice]
    indice = (indice + saut) % long

print(resu)