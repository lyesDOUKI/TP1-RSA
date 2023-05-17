#decouper un message en bloc
def decoupe_bloc(message, taille_bloc):
    blocs = []
    for i in range(0, len(message), taille_bloc):
        blocs.append(message[i:i+taille_bloc])
    for i in range(len(blocs)):
        if(len(blocs[i]) < taille_bloc):
            while(len(blocs[i]) < taille_bloc):
                #ajouter un espace a la fin
                blocs[i] += " "
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
def dechiffre(bloc, dictionnaire, taille_bloc):
    bloc_dechiifre = []
    mot_dechiffre = ""
    q = bloc
    taille_bloc = taille_bloc - 1
    while (taille_bloc >= 0):
        x = q // (len(dictionnaire) ** taille_bloc)
        q = q % (len(dictionnaire) ** (taille_bloc))
        bloc_dechiifre.append(x)
        taille_bloc -= 1
    for i in range(len(bloc_dechiifre)):
        for cle in dictionnaire:
            if dictionnaire[cle] == bloc_dechiifre[i]:
                mot_dechiffre += cle
    return mot_dechiffre, bloc_dechiifre
