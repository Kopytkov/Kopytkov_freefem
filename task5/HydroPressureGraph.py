import matplotlib.pyplot as plt
from collections import defaultdict

# Чтение данных из файла
data_file = "HydroPressure.txt"
data = defaultdict(list)

with open(data_file, "r") as file:
    for line in file:
        t, y, pressure = map(float, line.split())
        data[y].append((t, pressure))

# Построение графиков
for y, values in data.items():
    values.sort()  # Убедимся, что данные отсортированы по времени
    t_values, pressure_values = zip(*values)
    
    plt.figure()
    plt.plot(t_values, pressure_values, marker="o")
    plt.title(f"Pressure - Time for (x, y) = (0, {y})")
    plt.xlabel("Time, [s]")
    plt.ylabel("Pressure, [Pa]")
    plt.grid(True)
    plt.savefig(f"pressure_y_{y}.png")  # Сохранение графика
    plt.show()  # Показ графика

