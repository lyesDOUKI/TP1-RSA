import tp.utilities.calculArithm as  calculArithm
import tp.keysFonction.genration_keys as keysFonction
print("generation de clé publique et privée")
(e,n),(d,n) = keysFonction.generate_keys(20)
print("clé publique: ",e,n)
print("clé privée: ",d,n)