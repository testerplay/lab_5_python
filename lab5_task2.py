import numpy as np
import matplotlib.pyplot as plt

# Заданные параметры
U_0 = 0.1  # Начальное значение U[0]
T = 1.3    # Значение T
K = 4      # Константа K
xi = 0.7   # Коэффициент xi
T_0 = 2    # Параметр T0 (предположительно)

# Начальные условия
y = [0, 0]  # Начальные значения y[0] и y[1]

# Количество итераций
num_iterations = 100

# Вычисление значений y по рекуррентной формуле
for k in range(0, num_iterations - 2):  # Начинаем с 0, так как y[k+2] должно быть вычислено
    y_next = (2 - 2 * xi * T_0 / T) * y[k+1] + (2 * xi * T_0 / T - (T_0**2) / (T**2)) * y[k] + (K * T_0**2) / (T**2) * U_0
    y.append(y_next)

# Построение графика
x = np.arange(num_iterations)  # Индексы для оси x
plt.plot(x, y, label="y[k]", color="b")
plt.title("График y[k] по рекуррентной формуле")
plt.xlabel("Итерация k")
plt.ylabel("y[k]")
plt.grid(True)
plt.legend()
plt.show()
