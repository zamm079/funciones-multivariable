import numpy as np
import matplotlib.pyplot as plt

def rosenbrock_funt(X,Y):
    r = (100 * (Y - X**2)**2) + (1 - X)**2 
    return r

# x = np.linspace(-2, 2, 100)
# y = np.linspace(-1, 3, 100)
# X, Y = np.meshgrid(x, y)
# Z = rosenbrock_funt(X,Y)
# print(Z)
# print(rosenbrock_funt(1,1))

# contour_filled = plt.contourf(X, Y, Z, levels=100, cmap='viridis')
# plt.colorbar(contour_filled)
# contour_lines = plt.contour(X, Y, Z, levels=100, colors='white', linewidths=0.5)


# plt.title('función Rosenbrock')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
