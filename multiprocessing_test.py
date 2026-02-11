import time
from multiprocessing import Pool, cpu_count



# Функция, которая нагружает процессор (Вычисляет сумму квадратов)
def heavy_computation(n):
    result = 0
    for i in range(n):
        result += i * i
    return result


def run_benchmark():
    # Задача: 4 раза посчитать сумму до 20 миллионов
    tasks = [20_000_000] * 4

    print(f"Количество ядер CPU: {cpu_count()}")

    # 1. ПОСЛЕДОВАТЕЛЬНО (Один процесс)
    start = time.time()
    results = [heavy_computation(n) for n in tasks]
    end = time.time()
    print(f"🐢 Последовательно: {end - start:.2f} сек.")

    # 2. ПАРАЛЛЕЛЬНО (Multiprocessing)
    start = time.time()
    # Создаем пул процессов (количество = количеству ядер)
    with Pool(cpu_count()) as p:
        results = p.map(heavy_computation, tasks)
    end = time.time()
    print(f"🚀 Multiprocessing: {end - start:.2f} сек.")


if __name__ == "__main__":
    # В Windows multiprocessing ОБЯЗАН быть внутри if __name__ == "__main__"
    run_benchmark()