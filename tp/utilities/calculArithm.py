#fonction de calcul de pgcd
def pgcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def inverse_mod(phi, e):
    r1 = phi
    r2 = e
    u1 = 1
    u2 = 0
    v1 = 0
    v2 = 1
    while r2 != 0:
        q = r1 // r2
        rs = r1
        us = u1
        vs = v1
        r1 = r2
        u1 = u2
        v1 = v2
        r2 = rs - q * r2
        u2 = us - q * u2
        v2 = vs - q * v2
    print("phi = ",phi)
    print("e = ",e)
    print("r1 = ",r1)
    print("v1 = ",v1)
    print("u1 = ",u1)
    return r1, v1, u1
