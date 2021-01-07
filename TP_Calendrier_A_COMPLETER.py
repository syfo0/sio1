#TP Calendrier à  compléter

Mois=['janvier', 'février', 'mars', 'avril', 'mai', 'juin',
      'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

LongueurMois=[31,28,31,30,31,30,31,31,30,31,30,31]

RangFinMois=[31,0,0,0,0,0,0,0,0,0,0,0]

for i in range(1,12):  # 12 exclu, 11 inclus
    RangFinMois[i]=LongueurMois[i]+RangFinMois[i-1]


def Date(n): #n est un entier compris entre 1 et 365
    i=0
    while n> RangFinMois[i]:
        i=i+1
    #WhileEnd
    m= Mois[i]

    j=n-RangFinMois[i-1]

    resu =  str(j) +' '+m
    return resu


def Rang(j, m ):
    return 'Fonction à  compléter'

