#-------------------------------------------------------------------------------
# Name:   PISTES DE SKI

pistes=[['A','B','B','C','C','D','D','E','F'],
       ['B','C','E','A','D','A','E','F','D']]

parcours1='BEF'
parcours2='ABCDFDA'
parcours3='DABEFDA'


def piste_ouverte(debut, fin):
    global pistes
    valide=False
    for i in range(9):
        if pistes[0][i]==debut and pistes[1][i]==fin:
            valide=True
            return valide
    return valide

def parcours_valide(parcours):
    # fonction à compléter
    return

