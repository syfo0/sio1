# parcours d'une chaîne avec saut

chaine = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
long = len (chaine)


for saut in range(long):
    print(saut)
    indice = 0
    resu = ''
    for i in range(long):
        resu = resu + chaine[indice]
        indice = (indice + saut) % long
    print(resu)
    test = True
    i = 1
    while test and i<long:
        if resu[i]==chaine[0]:
            test = False
        i = i+1

    if test:
        print("tous les caractères sont présents")
    else:
        print('Problème : certains caractères sont répétés !')
    print()

