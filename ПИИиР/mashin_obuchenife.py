import numpy as np
import matplotlib.pyplot as plt

N = 50
mu, sigma = 0, 1
k, b = 3, 4 # параметры решающей функции
noise = np.random.normal(b, sigma, N)

x_train = np.linspace(0, 10, N) # измерения
y_train = k * x_train + noise # целевые значения

g = k * x_train + b # решающая функция

plt.scatter(x_train, y_train, color='red', label='y_train') # строим обучающую выборку
plt.plot(x_train, g, c='blue', label='g') # строим решающую функцию
plt.legend()
plt.savefig('plot6.png')