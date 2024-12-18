import matplotlib.pyplot as plt
from collections import defaultdict

# Чтение данных из файла
data_file = "HydroPressure.txt"
data = defaultdict(list)

with open(data_file, "r") as file:
    for line in file:
        t, y, pressure = map(float, line.split())
        data[y].append((t, pressure))

title = "Lower bound"
count = 0
# Построение графиков
for y, values in data.items():
    values.sort()  # Убедимся, что данные отсортированы по времени
    t_values, pressure_values = zip(*values)
    
    plt.figure()
    plt.plot(t_values, pressure_values, marker="o")
    if count == 0:
        plt.title(f"Pressure - Time for (x, y) = (0, {y}) \n {title}" )
        title = "Middle"
    if count == 1:
        plt.title(f"Pressure - Time for (x, y) = (0, {y}) \n {title}" )
        title = "Upper bound"
    if count == 2:
        plt.title(f"Pressure - Time for (x, y) = (0, {y}) \n {title}" )
    plt.xlabel("Time, [s]")
    plt.ylabel("Pressure, [Pa]")
    plt.grid(True)
    plt.savefig(f"pressure_y_{y}.png")
    plt.show()  # Показ графика
    count += 1
