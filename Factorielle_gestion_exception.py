# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:30:10 2022

@author: SAMIR MEBREK

FONCTION FACTORIELLE
"""

#### FONCTION Factorielle améliorée ###
def factorielle():
   """
   @factorielle
   Entrées: n de type entier
   Sorties: result de type entier
   Conseil: Utiliser les return pour une éventuelle utilisation prochaine du résultat
   Version: Ajout des exception:
       # Nombre négatifs ==> converti automatiquement en positif
       # Nombre complex ==> on prends la partie réelle et on averti l'user
       # Chaine de caractère ==> Boucle de message d'erreur et possibilité de retaper le nombre
       # Nombre à flotante ==> on prends que la partie entière et on averti l'user
       
   """
   # INTRODUCTION DES VALEURS ET GESTION DES EXCEPTION #
   n = input("Veuillez introduire nombre entier n: ")
   try:
       n=int(n)
   except ValueError:
       pass
   if type(n) == str:
        while (type(n) == str):
            try:
                n = int(input("n:"))
            except:
                print("Le str n'est pas castable en int")
                
   elif type(n) == complex():
       print("Attention, uniquement la partie réelle récupérée et utilisée")
       n = n.real
       
   elif n < 0:
       print("Attention, le nombre est converti automatiquement on nombre positif")
       n = -n
       
   elif type(n) == float:
       print("Attention, le nombre est converti automatiquement on un entier")
       n = int(n)
       
   # TRAITEMENT DE LA FONCTION #
   if n == 0:
       return 1
   else:
       F = 1
       for k in range(2,n+1):
          F = F * k
 
   return F


#### FONCTION MAIN ####
print("----------------------------------------------------------------")
print("------------Ceci est une fonction factorielle-------------------")
print("----------------------------------------------------------------")

print(factorielle())