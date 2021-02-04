# TP13

def valeur(car):
    """convertit au format entier un caractère compris entre 0 et F"""
    chiffre_list = '0123456789ABCDEF'
    resu = -1
    for i in range(len(chiffre_list)):
        if chiffre_list[i]==car :
            resu = i
    return resu

def convert (chaine):
    long = len (chaine)
    resu = 0
    expo = long - 1
    for i in range (long):
        chiffre = valeur(chaine[i])
        print(chiffre)
        print(expo)
        expo = expo -1
        
    return resu

