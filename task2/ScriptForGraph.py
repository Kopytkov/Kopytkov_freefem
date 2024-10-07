import matplotlib.pyplot as plt

def plot_data(filename, i):
    s_values = []
    u_values = []
    x1, y1 = 2.0, 3.0
    x2, y2 = 9.0, 7.0
    n = 50

    # Чтение файла
    with open(filename, 'r') as file:
        for line in file:
            s, u = map(float, line.split())
            s_values.append(s)
            u_values.append(u)

    # Построение графика
    plt.plot(s_values, u_values, marker='o')
    plt.xlabel('s (параметр отрезка)')
    plt.ylabel('u(s)')
    plt.title(f'Значения функции u вдоль отрезка \n [(x1; y1), (x2; y2)] = [({x1}; {y1}), ({x2}; {y2})]'
              + f'\n n = {n}; Номер итерации = {i + 1}')
    plt.grid(True)
    plt.show()

# Вывод графиков
for j in range (5):
    plot_data("C:\\Users\\suren\\.vscode\\OutputAdaptmesh" + str(j) + ".txt", j)
