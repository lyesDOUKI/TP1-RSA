import random

from tp.utilities.calcul_arithm import pgcd
from tp.utilities.calcul_arithm import inverse_mod
from tp.utilities.calcul_arithm import is_prime
from tp.utilities.calcul_arithm import factorize
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
    while(is_prime(p)==False):
        p = random.randint(2, 2**(nbits // 2))
    while(is_prime(q)==False and q != p):
        q = random.randint(2, 2**(nbits // 2))

    print("le p : ",p)
    print("le q : ",q)
    n= p*q
    #n = 755918011
    p, q = factorize(n)
    print("le p : ",p)
    print("le q : ",q)
    print("p * q = ",p*q)
    print("n = ",n)
    phi = (p-1)*(q-1)
    print("phi = ",phi)


    e = random.randint(2, 2**(nbits // 2))
    result_pgcd, d, k = inverse_mod(e, phi)
    while result_pgcd!=1:
        e = random.randint(2, 2**(nbits // 2))
        result_pgcd, d, k  = inverse_mod(e, phi)
    print("resultat de la fonction de l'algorthime d'euclide : ")
    if(d<0):
        d =d%phi
    print("e = ",e)
    print("pgcd = ",result_pgcd)
    print("k = ",k)
    print("d = ",d)

    return (e,n),(d,n)


