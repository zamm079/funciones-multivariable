import numpy as np
import math
import random

def simplex_search_meth(x,func,gama = 1.5,beta=0.2,epsilon=0.001):
    # step 1
    #no cero hipervolumen
    alpha=1
    N = len(x)
    d1 = ((math.sqrt(N+1)+N-1)/N*math.sqrt(2))*alpha
    d2 = ((math.sqrt(N+1)-1)/N*math.sqrt(2))*alpha

    
    
    

    return x



def sphere_func(x):
    r=0
    for i in x:
        r = r + (i**2)
    return r

print(simplex_search_meth(np.array([-1,1.5]),sphere_func))