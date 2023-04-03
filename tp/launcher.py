import math

import tp.utilities.calcul_arithm as  calculArithm
import tp.keysFonction.genration_keys as keysFonction
from tp.chiffDechiff.chiffrer_dechiffrer import chiffrer_dechiffrer
from tp.utilities.bloc_utilities import decoupe_bloc
from tp.utilities.bloc_utilities import convert_bloc_to_int
print("generation de clé publique et privée")
(e,n),(d,n) = keysFonction.generate_keys(16)
print("clé publique: ",e,n)
print("clé privée: ",d,n)
message =   31
print("chiffrer le message : ",message)
#si c'est une liste
if(isinstance(message, list)):
    listMessageDecry= []
    c= []
    for i in range(len(message)):
        tmp = chiffrer_dechiffrer(message[i], d, n)
        listMessageDecry.append(tmp)
    print("message déchiffré : ",listMessageDecry)
    for i in range(len(message)):
        tmp = chiffrer_dechiffrer(listMessageDecry[i], e, n)
        c.append(tmp)
    print("message chiffré : ",c)
else:
    #si c'est un entier
    message_chiffre = chiffrer_dechiffrer(message, e, n)
    print("message chiffré : ",message_chiffre)
    message_dechiffre = chiffrer_dechiffrer(message_chiffre, d, n)
    print("message déchiffré : ",message_dechiffre)

dictionnaire = {}

# Ajout des lettres de l'alphabet et de leurs valeurs
for i in range(1, 27):
    dictionnaire[chr(i + 64)] = i - 1

# Affichage du dictionnaire
dictionnaire["_"] = 26
dictionnaire[","] = 27
dictionnaire["?"] = 28
dictionnaire["€"] = 29
for i in range(30, 41):
    dictionnaire[i] = i-30
print(dictionnaire)
print("taille bloc ")
taille_bloc = (int)(math.log(n,40))
taille_bloc = taille_bloc
print( taille_bloc)
test = "message"
t = decoupe_bloc(test, taille_bloc)
print(t)
t = convert_bloc_to_int(t, dictionnaire)
print(t)
