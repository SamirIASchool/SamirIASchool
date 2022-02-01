# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:30:10 2022

@author: SAMIR MEBREK

FONCTION fibonacci
"""

def fibonacci(num):
    """
    Entrées: num de type entier
     
    Sorties: result de type liste
     
    Conseil: Utiliser les return pour une éventuelle utilisation prochaine du résultat
    """
    fibo = [0]*(n)
    fibo[0] = 0
    fibo[1] = 1

    for i in range(2,n):
        fibo[i] = fibo[i-1] + fibo[i-2]

    return fibo

#### FONCTION MAIN ####
print("----------------------------------------------------------------")
print("------------Ceci est une fonction fibonacci-------------------")
print("----------------------------------------------------------------")

n = int(input("Veuillez introduire nombre n= "))
print(fibonacci(n))
