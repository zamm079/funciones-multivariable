import numpy as np
import matplotlib.pyplot as plt

def sphere_function(X):
    r = np.sum(X**2,axis=0)
    return r

print(sphere_function(np.array([-1,1.5])))

# x = np.linspace(-2,2,100)
# y = np.linspace(-2,2,100)
# X,Y = np.meshgrid(x,y)
# z = np.array([X,Y])

# Z = sphere_function(z)
# print(Z)

# plt.figure(figsize=(8, 6))
# contour = plt.contour(X, Y, Z, 50, cmap='viridis')
# plt.colorbar(contour)
# plt.title('Contorno de la función Sphere')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()