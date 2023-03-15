import random

from tp.utilities.calculArithm import pgcd
from tp.utilities.calculArithm import inverse_mod

#fonction qui génère les clés publiques et privées
def generate_keys(nbits):
    #test avec exercice 4 TD2 fait le 15/03/2023
    #resultat positif avec les valeurs suivantes
    #p = 5
    #q = 11
    #e = 3
    #cle publique (e,n) = (3,55)
    #cle privée (d,n) = (27,55)
    p = random.randint(2, 2**(nbits // 2))
    q = random.randint(2, 2**(nbits // 2))
    while pgcd(p,q)!=1:
        p = random.randint(2, 2**(nbits // 2))
        q = random.randint(2, 2**(nbits // 2))
    n = p*q
    print("n = ",n)
    phi = (p-1)*(q-1)
    print("phi = ",phi)


    e = random.randint(2, 2**(nbits // 2))
    result_pgcd, d, k = inverse_mod(phi, e)
    while result_pgcd!=1:
        e = random.randint(2, 2**(nbits // 2))
        result_pgcd, k, d  = inverse_mod(phi, e)
    print("resultat de la fonction de l'algorthime d'euclide : ")
    print("e = ",e)
    print("pgcd = ",result_pgcd)
    print("k = ",k)
    print("d = ",d)
    return (e,n),(d,n)


