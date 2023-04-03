import tp.utilities.calcul_arithm as  calculArithm
import tp.keysFonction.genration_keys as keysFonction
from tp.chiffDechiff.chiffrer_dechiffrer import chiffrer_dechiffrer
print("generation de clé publique et privée")
(e,n),(d,n) = keysFonction.generate_keys(16)
print("clé publique: ",e,n)
print("clé privée: ",d,n)
message =   [671828605, 407505023, 288441355, 679172842, 180261802]
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