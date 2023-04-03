#decouper un message en bloc
def decoupe_bloc(message, taille_bloc):
    blocs = []
    for i in range(0, len(message), taille_bloc):
        blocs.append(message[i:i+taille_bloc])
    return blocs
#fonction qui convertit un bloc en bloc d'entier avec un dictonnaire
def convert_bloc_to_int(bloc, dictionnaire):
    bloc_int = []
    print("bloc ",bloc)
    for i in range(len(bloc)):
        tmp = []
        for j in range(len(bloc[i])):
            tmp.append(dictionnaire[bloc[i][j].upper()])
        bloc_int.append(tmp)
    return bloc_int
