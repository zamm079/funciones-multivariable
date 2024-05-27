import numpy as np
import matplotlib.pyplot as plt

def rastrigin(X):
    A = 10
    n = len(X)
    r = A * n + np.sum(X**2 - A * np.cos(2 * np.pi * X),axis=0)
    return r

# x = np.linspace(-5.12, 5.12, 100)
# y = np.linspace(-5.12, 5.12, 100)
# X, Y = np.meshgrid(x, y)
# z=np.array([X,Y])
# Z = rastrigin(z)


# plt.figure(figsize=(8, 6))
# contour = plt.contour(X, Y, Z, 50, cmap='viridis')
# plt.colorbar(contour)

# plt.title('Contorno de la función de Rastrigin')
# plt.xlabel('x')
# plt.ylabel('y')

# plt.show()
