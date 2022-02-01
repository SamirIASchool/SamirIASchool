# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:30:10 2022

@author: SAMIR MEBREK

FONCTION POLYNOMIALE
"""

#### FONCTION Polynome ###
def Polynome(a):
    """
    Entrées: a de type entier
    
    Sorties: result de type réel
    
    Conseil: Utiliser les return pour une éventuelle utilisation prochaine du résultat
    """
    
    result = pow(a, 3) - 1.5*(x**2) -6*x + 5
    
    
    return result


#### FONCTION MAIN ####
print("----------------------------------------------------------------")
print("------------Ceci est une fonction polynomiale-------------------")
print("-------------X^3 - 1,5² - 6x + 5--------------------------------")
print("----------------------------------------------------------------")

x = int(input("Veuillez introduire la variable x: "))
print(Polynome(x))


