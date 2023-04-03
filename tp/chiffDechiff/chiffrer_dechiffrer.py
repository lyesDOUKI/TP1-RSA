def chiffrer_dechiffrer(message, cle, modulo):
    #return (message**cle)%modulo
    return pow(message, cle, modulo)