import math

import tp.utilities.calcul_arithm as calculArithm
import tp.keysfonction.genration_keys as keysFonction
from tp.chiffdechiff.chiffrer_dechiffrer import chiffrer_dechiffrer
from tp.utilities.bloc_utilities import decoupe_bloc, convert_bloc_to_lettre, dechiffre
from tp.utilities.bloc_utilities import convert_bloc_to_int
from tp.utilities.bloc_utilities import chiffrer_bloc

print("generation de clé publique et privée")
(e, n), (d, n) = keysFonction.generate_keys(16)
print("clé publique: ", e, n)
print("clé privée: ", d, n)
message = 31
print("chiffrer le message : ", message)
# si c'est une liste
taille_liste = 0
if (isinstance(message, list)):
    taille_liste = len(message)
    listMessageDecry = []
    c = []
    for i in range(taille_liste):
        tmp = chiffrer_dechiffrer(message[i], d, n)
        listMessageDecry.append(tmp)
    print("message déchiffré : ", listMessageDecry)
    for i in range(taille_liste):
        tmp = chiffrer_dechiffrer(listMessageDecry[i], e, n)
        c.append(tmp)
    print("message chiffré : ", c)
else:
    # si c'est un entier
    message_chiffre = chiffrer_dechiffrer(message, e, n)
    print("message chiffré : ", message_chiffre)
    message_dechiffre = chiffrer_dechiffrer(message_chiffre, d, n)
    print("message déchiffré : ", message_dechiffre)

dictionnaire = {}

# Ajout des lettres de l'alphabet et de leurs valeurs
for i in range(1, 27):
    dictionnaire[chr(i + 64)] = i - 1

# Affichage du dictionnaire
dictionnaire["_"] = 26
dictionnaire[","] = 27
dictionnaire["?"] = 28
dictionnaire["€"] = 29
dictionnaire[" "] = 30
dictionnaire["a"] = 31
dictionnaire["b"] = 32
dictionnaire["c"] = 33
dictionnaire["d"] = 34
dictionnaire["e"] = 35
dictionnaire["f"] = 36
dictionnaire["g"] = 37
dictionnaire["h"] = 38
dictionnaire["i"] = 39
dictionnaire["j"] = 40
print(dictionnaire)
taille_bloc = int((math.log(n, 41)))
print("taille du bloc : ", taille_bloc)
message_a_chiffrer = "je reussi a chiffrer un message, et ouais c est cool"
if(len(message_a_chiffrer) % taille_bloc != 0):
    print("le message n'est pas divisible par la taille du bloc, on ajoute des espaces")
    message_a_chiffrer = " " + message_a_chiffrer
list_des_bloc = decoupe_bloc(message_a_chiffrer, taille_bloc)
print("decoupage du message en bloc :  ", list_des_bloc)
list_des_bloc_chiffre = convert_bloc_to_int(list_des_bloc, dictionnaire)
print("chiffrage message decoupé en nombres : ", list_des_bloc_chiffre)
list_des_bloc_chiffre_int = []
for i in range(len(list_des_bloc_chiffre)):
    tmp = chiffrer_bloc(list_des_bloc_chiffre[i], 40)
    list_des_bloc_chiffre_int.append(tmp)
print("etape 1 : chiffrage des lettres en nombres chiffré : ", list_des_bloc_chiffre_int)
# chiffrer les blocs
chiffrage_bloc = []
for i in range(len(list_des_bloc_chiffre_int)):
    tmp = chiffrer_dechiffrer(list_des_bloc_chiffre_int[i], e, n)
    chiffrage_bloc.append(tmp)
print("etape 2 : chiffrage des nombres chiffrée (etape 1)  : ", chiffrage_bloc)
# parcourir chiffrage_bloc
list_msg_chiffre = []
for i in range(len(chiffrage_bloc)):
    if(chiffrage_bloc[i] > 40**taille_bloc):
        #print("trop grand pour rester sur la meme taille de bloc, valeur du bloc : ",
         #    chiffrage_bloc[i], " > ", 40**2, "40 ** taille_bloc")
        taille_blocV2 = taille_bloc + 1
        recup = dechiffre(chiffrage_bloc[i], dictionnaire, taille_blocV2)
        list_msg_chiffre.append(recup)
    else:
        recup = dechiffre(chiffrage_bloc[i], dictionnaire, taille_bloc)
        list_msg_chiffre.append(recup)
print("etape 3 : message chiffré en lettres : ", list_msg_chiffre)
# construction du message
message_chiffre_final = ""
for i in range(len(list_msg_chiffre)):
    message_chiffre_final += list_msg_chiffre[i]
print("etape 4 : message chiffré final : ", message_chiffre_final)
dechiffrage_bloc = []
for i in range(len(chiffrage_bloc)):
    tmp = chiffrer_dechiffrer(chiffrage_bloc[i], d, n)
    dechiffrage_bloc.append(tmp)
print("etape 5 : dechiffrage du message chiffrée en nombres : ", dechiffrage_bloc)
# affichage message original
message_original = []
for i in range(len(chiffrage_bloc)):
        recupere_mot = dechiffre(list_des_bloc_chiffre_int[i], dictionnaire, taille_bloc)
        message_original.append(recupere_mot)
print("etape 6 : nombres chiffrée en lettres : ", message_original)
#construction du message
message_final = ""
for i in range(len(message_original)):
    message_final += message_original[i]
if(message_final == message_a_chiffrer.upper()):
    print("felicitation, le message a bien été chiffré et déchiffré")
    print("message à chiffré : ", message_a_chiffrer.upper())
    print("message chiffré  : ", message_chiffre_final)
    print("message déchiffré : ", message_final)
    print("fin du programme")