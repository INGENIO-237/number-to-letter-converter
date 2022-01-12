unites = {
    0: 'ZERO',
    1: 'UN',
    2: 'DEUX',
    3: 'TROIS',
    4: 'QUATRE',
    5: 'CINQ',
    6: 'SIX',
    7: 'SEPT',
    8: 'HUIT',
    9: 'NEUF',
}
dizaines ={
    11: 'ONZE',
    12: 'DOUZE',
    13: 'TREIZE',
    14: 'QUATORZE',
    15: 'QUINZE',
    16: 'SEIZE',
    17: 'DIX-SEPT',
    18: 'DIX-HUIT',
    19: 'DIX-NEUF',
}
dizaines_zero = {
    10: 'DIX',
    20: 'VINGT',
    30: 'TRENTE',
    40: 'QUATORZE',
    50: 'CINQUANTE',
    60: 'SOIXANTE',
    70: 'SOIXANTE DIX',
    80: 'QUATRE-VINGT',
    90: 'QUATRE-VINGT DIX'
}

centaine = {
    100: 'CENT'
}


def lettre(num):
    def deux_chiffres(num_2):
        #Lorsque le nombre est de la forme 01, 02,....., 09
        if num_2[0] == '0':
            return unites[int(num_2[1])]
        # Si le nombre est paire de la forme (10, 20, 30, 40,......, 90)
        if num_2[1] == '0':
            return dizaines_zero[int(num_2)]
        # Si le nombre est compris entre 11 et 19
        elif num_2[1] != '0' and num_2[0] == '1':
            return dizaines[int(num_2)]
        # Si le nombre est formé de deux chiffres à valeurs quelconques
        elif num_2[1] != '0' and num_2[0] != '1':
            return dizaines_zero[int(num_2) - int(num_2[1])] + " " + unites[int(num_2[1])]

    def trois_chiffres(num_3):
        # Si le nombre est de la forme 010, 011, ...., 099
        if num_3[0] == '0':
            return deux_chiffres(num_3[1:])
        # Si le nombre vaut 100
        if num_3[0] == '1' and num_3[1] == '0' and num_3[2] == '0':
            return centaine[100]
        # Si le nombre est formé de 3 chiffres que le premier est == 1
        elif num_3[0] == '1':
            # Si le deuxieme chiffre == 0 mais que le troisieme != 0
            if num_3[1] == '0' and num_3[2] != '0':
                return centaine[100] + " " + unites[int(num_3[2])]
            # Si le deuxieme chiffre est != 0
            # L'on fait appel à la fonction 'deux_chiffres' pour trouver sa correspondance en lettres
            elif num_3[1] != '0':
                a = num_3[1:]
                return centaine[100] + " " + deux_chiffres(a)
        # Si le premier chiffre est != 1
        elif num_3[0] != '1':
            # Lorsque le deuxieme chiffre == 0 mais que le troisieme != 0
            if num_3[1] == '0' and num_3[2] != '0':
                return unites[int(num_3[0])] + " " + centaine[100] + " " + unites[int(num_3[2])]
            # Si le deuxieme chiffre est != 0
            # L'on fait appel à la fonction 'deux_chiffres' pour trouver sa correspondance en lettres
            if num_3[1] != '0':
                a = num_3[1:]
                return unites[int(num_3[0])] + " " + centaine[100] + " " + deux_chiffres(a)

    if len(num) == 1:
        return unites[int(num)]
    elif len(num) == 2:
        return deux_chiffres(num)
    elif len(num) == 3:
        return trois_chiffres(num)


number = input('Entrer un nombre : ')

print(lettre(number))
