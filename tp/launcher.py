import math
import keysfonction.genration_keys as keysFonction
from chiffdechiff.chiffrer_dechiffrer import chiffrer_dechiffrer
from utilities.bloc_utilities import decoupe_bloc, dechiffre
from utilities.bloc_utilities import convert_bloc_to_int
from utilities.bloc_utilities import chiffrer_bloc

print("generation de clé publique et privée")
(e, n), (d, n) = keysFonction.generate_keys(32)
print(" -clé publique: ", e, n)
print(" -clé privée: ", d, n)
message = 123
print("##################################################")
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
print("##################################################")
dictionnaire = {}

# Ajout des lettres de l'alphabet et de leurs valeurs
for i in range(1, 27):
    dictionnaire[chr(i + 64)] = i - 1

# Affichage du dictionnaire
dictionnaire["_"] = 26
dictionnaire[","] = 27
dictionnaire["?"] = 28
dictionnaire["€"] = 29
dictionnaire["0"] = 30
dictionnaire["1"] = 31
dictionnaire["2"] = 32
dictionnaire["3"] = 33
dictionnaire["4"] = 34
dictionnaire["5"] = 35
dictionnaire["6"] = 36
dictionnaire["7"] = 37
dictionnaire["8"] = 38
dictionnaire["9"] = 39
dictionnaire[" "] = 40
print(dictionnaire)
taille_bloc = int((math.log(n, len(dictionnaire))))
print("taille du bloc : ", taille_bloc)
message_a_chiffrer = input("tu veux chiffrer quoi?\n")
list_des_bloc = decoupe_bloc(message_a_chiffrer, taille_bloc)
print("etape 0a : decoupage du message en bloc :  ", list_des_bloc)
list_des_bloc_chiffre = convert_bloc_to_int(list_des_bloc, dictionnaire)
print("etape 0b  : chiffrage message decoupé en nombres : ", list_des_bloc_chiffre)
list_des_bloc_chiffre_int = []
for i in range(len(list_des_bloc_chiffre)):
    tmp = chiffrer_bloc(list_des_bloc_chiffre[i], len(dictionnaire))
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
list_msg_chiffre_int = []
taille_blocV2 = 0
i = 0
while(taille_blocV2 == 0 and i < len(chiffrage_bloc)):
    if(chiffrage_bloc[i] > len(dictionnaire)**taille_bloc):
        print("!!!!!!!!! la taille du bloc change !!!!!!!!!")
        taille_blocV2 = taille_bloc + 1
        print("!!!!!!!!! nouvelle taille du bloc : ", taille_blocV2, " !!!!!!!!!")
    i = i + 1
if(taille_blocV2 != 0):

    for i in range(len(chiffrage_bloc)):
        recup_lettre, recup_chiffre = dechiffre(chiffrage_bloc[i], dictionnaire, taille_blocV2)
        list_msg_chiffre.append(recup_lettre)
        list_msg_chiffre_int.append(recup_chiffre)
else:
    for i in range(len(chiffrage_bloc)):
        recup_lettre, recup_chiffre = dechiffre(chiffrage_bloc[i], dictionnaire, taille_bloc)
        list_msg_chiffre.append(recup_lettre)
        list_msg_chiffre_int.append(recup_chiffre)
print("etape 3a : dechiffrage du message chiffrée en nombres : ", list_msg_chiffre_int)
print("etape 3b : dechiffrage du message chiffrée en lettres : ", list_msg_chiffre)
list_last_chiffrage = []
for i in range(len(list_msg_chiffre_int)):
    last_chiffrage = chiffrer_bloc(list_msg_chiffre_int[i], len(dictionnaire))
    list_last_chiffrage.append(last_chiffrage)
print("etape 3c : chiffrage du message déchiffrée en nombres : ", list_last_chiffrage)
# construction du message
message_chiffre_final = ""
for i in range(len(list_msg_chiffre)):
    message_chiffre_final += list_msg_chiffre[i]
dechiffrage_bloc = []
for i in range(len(list_last_chiffrage)):
    tmp = chiffrer_dechiffrer(list_last_chiffrage[i], d, n)
    dechiffrage_bloc.append(tmp)
print("etape 4 : dechiffrage du message chiffrée en nombres : ", dechiffrage_bloc)
# affichage message original
message_original = []
for i in range(len(chiffrage_bloc)):
        recupere_mot, recupere_int = dechiffre(list_des_bloc_chiffre_int[i], dictionnaire, taille_bloc)
        message_original.append(recupere_mot)
print("etape 5 : nombres chiffrée en lettres : ", message_original)
print("etape 6 : decoupage en entiers correspondant au lettres : ", convert_bloc_to_int(
    message_original, dictionnaire)
)
#construction du message
message_final = ""
for i in range(len(message_original)):
    message_final += message_original[i]
message_final = message_final[0:len(message_a_chiffrer)]
if(message_final == message_a_chiffrer.upper()):
    print("felicitation, le message a bien été chiffré et déchiffré")
    print("message à chiffré : ", message_a_chiffrer.upper())
    print("message chiffré  : ", message_chiffre_final)
    print("message déchiffré : ", message_final)
    print("fin du programme")
