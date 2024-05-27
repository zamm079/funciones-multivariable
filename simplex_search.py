import numpy as np
import math
from funciones_prueba.sphere_funcion import sphere_function

def simplex_search_meth(x,func,gama=1.5,beta=0.2,epsilon=0.001):
    # step 1
    #no cero hipervolumen
    alpha=1
    N = len(x)
    d1 = ((math.sqrt(N+1)+N-1)/N*math.sqrt(2))*alpha
    d2 = ((math.sqrt(N+1)-1)/N*math.sqrt(2))*alpha
    simplex = np.zeros((N + 1,N))
    for i in range(len(simplex)):
        for j in range(N):
            if j == i:
                simplex[i,j] = x[j]+d1
            if j != i:
                simplex[i,j] = x[j]+d2
    i_max = 1000
    i = 0

    # step 2
    f_values = np.apply_along_axis(func, 1, simplex)
    xi=0
    while i < i_max:
        val_orden = np.argsort(f_values)
        simplex = simplex[val_orden]
        xl,xg,xh = f_values[val_orden]
        #Xc
        xc = np.mean(simplex[:-1],axis=0)
        i+=1
        #step 3
        xr = 2*xc - xh
        xnew = xr
        if func(xr) < func(xl):
            xnew = (1+gama)*xc - (gama*xh) 
        elif func(xr) >= func(xh):
            xnew = (1-beta)*xc+(beta*xh)
        elif func(xg) < func(xr) < func(xh):
            xnew = (1+beta)*xc-(beta*xh)
        xh = xnew
        #step 4
        xi= np.sum(func(simplex))
        term1=(xi-xc)**2/(N+1)
        print('term1',term1)
        if term1**0.5 < epsilon:
            break
    return xnew


print("prueba ",simplex_search_meth(np.array([-1,1.5]),sphere_function))