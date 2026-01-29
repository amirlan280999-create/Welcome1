# ЗАДАНИЕ 5: "Вложенный поиск"
map_grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

print("Карта:")
for row in map_grid:
    print(row)

print("\nПоиск клада...")

found = False  # Флаг для остановки циклов

# Внешний цикл по строкам (индекс i = ось Y)
for i in range(len(map_grid)):
    # Внутренний цикл по столбцам (индекс j = ось X)
    for j in range(len(map_grid[i])):
        print(f"Проверяем клетку [{i}][{j}] = {map_grid[i][j]}")

        if map_grid[i][j] == 1:
            print(f"Клад найден на координатах ({j}, {i})")
            found = True
            break  # Прерываем внутренний цикл

    if found:
        break  # Прерываем внешний цикл

if not found:
    print(" Клад не найден!")
    