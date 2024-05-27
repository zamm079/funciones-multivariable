import numpy as np
import matplotlib.pyplot as plt

def Himmelblaus_function(x):
    r = (x**2 + x - 11)**2 + (x + x**2 -7)**2
    return r


# print(Himmelblaus_function(np.array([-1,1.5])))

# x = np.linspace(-5,5,100)
# y = np.linspace(-5,5,100)
# X,Y = np.meshgrid(x,y)
# Z = Himmelblaus_function(X,Y)
# print(Z)


# plt.figure(figsize=(10, 8))
# contour_filled = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
# plt.colorbar(contour_filled, label='Valores de Z')
# contour_lines = plt.contour(X, Y, Z, levels=50, colors='white', linewidths=0.5)
# plt.title('Contorno de la función Himmelblau', fontsize=14)
# plt.xlabel('x', fontsize=12)
# plt.ylabel('y', fontsize=12)
# plt.xlim([-5, 5])
# plt.ylim([-5, 5])
# plt.show()