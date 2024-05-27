import numpy as np

def nelder_mead(func, x_start, tol=1e-6, max_iter=1000):
    """
    Minimiza la función `func` usando el método de Nelder-Mead.
    
    Parameters:
    func : callable
        La función a minimizar.
    x_start : array_like
        El punto inicial para el algoritmo.
    tol : float, opcional
        La tolerancia para la convergencia. El valor predeterminado es 1e-6.
    max_iter : int, opcional
        El número máximo de iteraciones. El valor predeterminado es 1000.
    
    Returns:
    res : dict
        Un diccionario que contiene la solución encontrada y el número de iteraciones.
    """
    # Parámetros del algoritmo
    alpha = 1.0
    gamma = 2.0
    rho = 0.5
    sigma = 0.5

    # Inicializar el simplex
    n = len(x_start)
    simplex = np.zeros((n + 1, n))
    simplex[0] = x_start
    for i in range(n):
        y = np.array(x_start, copy=True)
        y[i] += 0.05 if x_start[i] == 0 else 0.05 * x_start[i]
        simplex[i + 1] = y

    # Evaluar la función en los vértices del simplex
    f_values = np.apply_along_axis(func, 1, simplex)
    iter_count = 0
    print(simplex)
    while iter_count < max_iter:
        # Ordenar el simplex por los valores de la función
        indices = np.argsort(f_values)
        simplex = simplex[indices]
        f_values = f_values[indices]

        # Centroid de los mejores n puntos
        centroid = np.mean(simplex[:-1], axis=0)

        # Reflejar
        xr = centroid + alpha * (centroid - simplex[-1])
        fxr = func(xr)

        if fxr < f_values[0]:
            # Expansión
            xe = centroid + gamma * (xr - centroid)
            fxe = func(xe)
            if fxe < fxr:
                simplex[-1] = xe
                f_values[-1] = fxe
            else:
                simplex[-1] = xr
                f_values[-1] = fxr
        else:
            if fxr < f_values[-2]:
                simplex[-1] = xr
                f_values[-1] = fxr
            else:
                # Contracción
                xc = centroid + rho * (simplex[-1] - centroid)
                fxc = func(xc)
                if fxc < f_values[-1]:
                    simplex[-1] = xc
                    f_values[-1] = fxc
                else:
                    # Reducción
                    for i in range(1, len(simplex)):
                        simplex[i] = simplex[0] + sigma * (simplex[i] - simplex[0])
                    f_values = np.apply_along_axis(func, 1, simplex)
        
        iter_count += 1

        # Verificar convergencia
        if np.max(np.abs(simplex[0] - simplex[1:])) < tol:
            break
    print(simplex)
    return {
        'x': simplex[0],
        'fval': f_values[0],
        'iterations': iter_count
    }

# Ejemplo de uso
def rosenbrock(x):
    return sum(100.0 * (x[1:] - x[:-1]**2.0)**2.0 + (1 - x[:-1])**2.0)

result = nelder_mead(rosenbrock, np.array([0.0, 0.0]))
print("Solución encontrada:", result['x'])
print("Valor de la función:", result['fval'])
print("Número de iteraciones:", result['iterations'])
