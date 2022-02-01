# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:30:10 2022

@author: SAMIR MEBREK

FONCTION FACTORIELLE
"""

#### FONCTION Polynome ###
def factorielle(n):
   """
   Entrées: n de type entier
    
   Sorties: result de type entier
    
   Conseil: Utiliser les return pour une éventuelle utilisation prochaine du résultat
   """
    
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

n = int(input("Veuillez introduire n: "))
print(factorielle(n))
