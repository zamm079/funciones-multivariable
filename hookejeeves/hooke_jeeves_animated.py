import numpy as np
import matplotlib.pyplot as plt



def hooke_jeeves(func, x0, step_size=0.5, step_reduction=0.5, tolerance=1e-6, max_iterations=1000):
    n = len(x0)
    x = np.array(x0)
    step = np.full(n, step_size)
    
    points = [x0]  

    def explore(base_point, step):
        new_point = np.copy(base_point)
        for i in range(n):
            for direction in [1, -1]:
                candidate = np.copy(new_point)
                candidate[i] += direction * step[i]
                if func(candidate) < func(new_point):
                    new_point = candidate
                    break
        return new_point

    iteration = 0
    while np.max(step) > tolerance and iteration < max_iterations:
        new_point = explore(x, step)
        if func(new_point) < func(x):
            x = new_point
        else:
            step = step * step_reduction
        iteration += 1
        points.append(np.copy(x))  
        print(f"Iteration {iteration}, x: {x}, f(x): {func(x)}")

    return x, points  

def objective_function(x):
    return (x[0] - 1)**2 + (x[1] - 2)**2


x0 = [-1, 1.5]


result, points = hooke_jeeves(objective_function, x0)

print("Resultado:", result)
print("Points:", points)

fig, ax = plt.subplots()
ax.set_xlim(-2, 3)
ax.set_ylim(-1, 4)
contour_x = np.linspace(-2, 3, 400)
contour_y = np.linspace(-1, 4, 400)
X, Y = np.meshgrid(contour_x, contour_y)
Z = objective_function([X, Y])
ax.contour(X, Y, Z, levels=50)


for i in range(1, len(points)):
    x_values = [points[i-1][0], points[i][0]]
    y_values = [points[i-1][1], points[i][1]]
    ax.plot(x_values, y_values, 'ro-')
    plt.pause(0.5)

plt.show()