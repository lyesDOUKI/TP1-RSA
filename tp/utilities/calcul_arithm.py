#fonction de calcul de pgcd
import random
def pgcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def inverse_mod(a, b):
    r, r_prime = a, b
    u, v, u_prime, v_prime = 1, 0, 0, 1
    while(r_prime != 0):
        q = r // r_prime
        rs, us, vs = r, u, v
        r, u, v = r_prime, u_prime, v_prime
        r_prime = rs - q * r_prime
        u_prime = us - q * u_prime
        v_prime = vs - q * v_prime
    return (r, u, v)

#fonction de nombre premier
"""
def is_prime(n):
    if n < 2:
        return False
    if(n%2==0):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
"""
#algorithme de miller rabin
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n%2==0:
        return False
    r = 0
    d = n-1
    while d%2==0:
        d = d//2
        r += 1
    for i in range(100):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x==1 or x==n-1:
            continue
        for j in range(r-1):
            x = pow(x, 2, n)
            if x==1:
                return False
            if x==n-1:
                break
        else:
            return False
    return True
#fonction qui genere nombre premier
def generate_prime(nbits):
    p = random.getrandbits(nbits)
    while not is_prime(p):
        p = random.getrandbits(nbits)
    return p
#fonction qui factorise un nombre en produit de deux nombres premiers
def factorize(n):
    p = 2
    while n % p != 0:
        p += 1
    return p, n // p
#convertir int to lettre
def convert_int_to_lettre(bloc, dictionnaire):
    bloc_lettre = []
    for i in range(len(bloc)):
        tmp = []
        for j in range(len(bloc[i])):
            tmp.append(dictionnaire[bloc[i][j]])
        bloc_lettre.append(tmp)
    return bloc_lettre