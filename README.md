# TP1-RSA
tp1 du module sécurité informatique en python
 -Génération de clés RSA
 -Chiffrage d'un mot ou phrase
 -Déchiffrage en utilisant l'algorithme RSA

Explication des quelques fonctionnalité du code : 
package : chiffdechiff : 
    cette fonction permet de chiffrer et déchiffrer un message en utilisant l'algorithme RSA
package : keyfonction : 
      les fonctions de ce packages permettent dans un premier temps de générer les clés RSA,
      aussi j'utilise l'algorithme d'inverse modulo pour calculer la clé privée.
package : utilities : 
    fichier bloc_utilites.py : 
        les fonctions de ce fichier permettent de découper un message en blocs de taille donnée en parametre
        et de les convertir en entier et vice versa.
    fichier calcul_arithm.py : 
        les fonctions de ce fichier permettent de calculer le pgcd, l'inverse modulo, verifier si un nombre est premier
        Aussi la fonction factorize(n) permet de factoriser un nombre n en utilisant l'algorithme de fermat.