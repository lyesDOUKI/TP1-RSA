#decouper un message en bloc
def decoupe_bloc(message, taille_bloc):
    blocs = []
    for i in range(0, len(message), taille_bloc):
        blocs.append(message[i:i+taille_bloc])
    return blocs
#fonction qui convertit un bloc en bloc d'entier avec un dictonnaire
def convert_bloc_to_int(bloc, dictionnaire):
    bloc_int = []
    for i in range(len(bloc)):
        tmp = []
        for j in range(len(bloc[i])):
            tmp.append(dictionnaire[bloc[i][j].upper()])
        bloc_int.append(tmp)
    return bloc_int
#convert bloc to letter
def convert_bloc_to_lettre(bloc, dictionnaire):
    bloc_lettre = []
    for i in range(len(bloc)):
        tmp = []
        for j in range(len(bloc[i])):
            tmp.append(dictionnaire[bloc[i][j].upper()])
        bloc_lettre.append(tmp)
    return bloc_lettre
#fonction qui chiffre un bloc
def chiffrer_bloc(bloc, taille_dictionnaire):
    bloc_chiffre = 0
    for i in range(len(bloc)):
        bloc_chiffre += bloc[i] * (taille_dictionnaire ** (len(bloc) - i - 1))
    return bloc_chiffre

#fonction qui dechiffre un bloc en lettres
def dechiffrer_bloc(bloc, taille_dictionnaire, dictionnaire):
    bloc_dechiffre = []
    while bloc > 0:
        bloc_dechiffre.append(bloc % taille_dictionnaire)
        bloc = bloc // taille_dictionnaire
    bloc_dechiffre.reverse()
    for i in range(len(bloc_dechiffre)):
        bloc_dechiffre[i] = dictionnaire[bloc_dechiffre[i]]
    return bloc_dechiffre
#fonction qui dechiffre un bloc en entier
def dechiffre(bloc, dictionnare, taille_bloc):
    if(taille_bloc == 2):
        valeur = 0
        i = 0
        j = 0
        indice1 = -1
        indice2 = -1
        for i in range(40):
            for j in range(40):
                valeur = i * pow(40, 1) + j * pow(40, 0)
                if valeur == bloc:
                    indice1 = i
                    indice2 = j
                    break

        if(indice1 != -1 and indice2 != -1):
            lettre1 = ""
            lettre2 = ""
            for cle in dictionnare:
                if dictionnare[cle] == indice1:
                    lettre1 = cle

                if dictionnare[cle] == indice2:
                    lettre2 = cle
            mot = str(lettre1) + str(lettre2)
            return mot
    elif(taille_bloc == 3):
        valeur = 0
        i = 0
        j = 0
        k = 0
        indice1 = -1
        indice2 = -1
        indice3 = -1
        for i in range(40):
            for j in range(40):
                for k in range(40):
                    valeur = i * pow(40, 2) + j * pow(40, 1) + k * pow(40, 0)
                    if valeur == bloc:
                        indice1 = i
                        indice2 = j
                        indice3 = k
                        break

        if(indice1 != -1 and indice2 != -1 and indice3 != -1):
            lettre1 = ""
            lettre2 = ""
            lettre3 = ""
            for cle in dictionnare:
                if dictionnare[cle] == indice1:
                    lettre1 = cle

                if dictionnare[cle] == indice2:
                    lettre2 = cle

                if dictionnare[cle] == indice3:
                    lettre3 = cle
            mot = str(lettre1) + str(lettre2) + str(lettre3)
            return mot
    elif(taille_bloc == 1):
        valeur = 0
        i = 0
        indice1 = -1
        for i in range(40):
            valeur = i * pow(40, 0)
            if valeur == bloc:
                indice1 = i
                break

        if(indice1 != -1):
            lettre1 = ""
            for cle in dictionnare:
                if dictionnare[cle] == indice1:
                    lettre1 = cle
            mot = str(lettre1)
            return mot