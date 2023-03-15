import tp.utilities.calcul_arithm as  calculArithm
import tp.keysFonction.genration_keys as keysFonction
from tp.chiffDechiff.chiffrer_dechiffrer import chiffrer_dechiffrer
print("generation de clé publique et privée")
(e,n),(d,n) = keysFonction.generate_keys(10)
print("clé publique: ",e,n)
print("clé privée: ",d,n)
message = 2
print("chiffrer le message : ",message)
message_chiffre = chiffrer_dechiffrer(message, e, n)
print("message chiffré : ",message_chiffre)
message_dechiffre = chiffrer_dechiffrer(message_chiffre, d, n)
print("message déchiffré : ",message_dechiffre)