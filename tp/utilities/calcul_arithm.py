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
def is_prime(n):
    if n < 2:
        return False
    if(n%2==0):
        return False
    for i in range(2, n):
        if n % i == 0:
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