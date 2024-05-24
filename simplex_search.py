import numpy as np
import math

def simplex_search_meth(x,func,gama,beta,epsilon):
    #no cero hipervolumen
    alpha=1
    N = len(x)
    d1 = ((math.sqrt(N+1)+N-1)/N*math.sqrt(2))*alpha
    d2 = ((math.sqrt(N+1)-1)/N*math.sqrt(2))*alpha
    print(d1,d2)
    for i in range(0,N):
        for j in range(0,N):
            if j == i:
                x[j]+d1
            if j != i:
                x[j]+d2
            print(f"i={i} j={j}")

    return x



def sphere_func(x):
    r=0
    for i in x:
        r = r + (i**2)
    return r

print(simplex_search_meth(np.array([-1,1.5]),sphere_func,0.5,0.1,0.001))