import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter=100):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

width, height = 800, 600
x = np.linspace(-2.5, 1, width)
y = np.linspace(-1.2, 1.2, height)

matrix = np.zeros((height, width))
for i, yi in enumerate(y):
    for j, xi in enumerate(x):
        matrix[i, j] = mandelbrot(complex(xi, yi))

plt.figure(figsize=(12, 8))
plt.imshow(matrix, cmap='inferno', extent=[-2.5, 1, -1.2, 1.2])
plt.colorbar()
plt.title('Mandelbrot Fractal', color='white', fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()
