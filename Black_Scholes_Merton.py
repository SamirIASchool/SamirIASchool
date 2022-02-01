from math import log, sqrt, exp
from scipy.stats import norm



#FONCTIONS QUI GERE LES VARIABLES d1 et d2
def d1(S,X,T,r,sigma):
    return(log(S/X)+(r+sigma**2/2.)*T)/(sigma*sqrt(T))

def d2(S,X,T,r,sigma):
    return d1(S,X,T,r,sigma)-sigma*sqrt(T)


#FONCTIONS DE CALL OPTION
def call_option(S,X,T,r,sigma):
    return S*norm.cdf(d1(S,X,T,r,sigma))-X*exp(-r*T)*norm.cdf(d2(S,X,T,r,sigma))
  
    
#FONCTIONS DE PUT OPTION
def put_option(S,X,T,r,sigma):
    return X*exp(-r*T)-S+call_option(S, X, T, r, sigma)(S,X,T,r,sigma)
