# parcours d'une chaine avec saut

chaine = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
long = len (chaine)
saut = int (input('Entrer la valeur du saut'))
indice = 0
resu = ''

for i in range(long):
    resu = resu + chaine[indice]
    indice = (indice + saut) % long

print(resu)