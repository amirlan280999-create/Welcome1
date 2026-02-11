import threading
import time

# Общий ресурс (Счет в банке)
bank_account = 0
# Замок (Аналог БлокировкаДанных в 1С)
lock = threading.Lock()


def deposit(count, use_lock):
    global bank_account
    for _ in range(count):
        if use_lock:
            # 🔒 БЕЗОПАСНО: Занимаем ресурс
            with lock:
                current = bank_account
                # Имитация микро-задержки, чтобы увеличить шанс ошибки
                # time.sleep(0.000001)
                bank_account = current + 1
        else:
            # 🔓 ОПАСНО: Гонка данных
            # Операция += 1 не атомарна!
            # Поток может быть прерван между чтением и записью.
            bank_account += 1


def run_test(use_lock):
    global bank_account
    bank_account = 0
    print(f"--- Тест {'С ЗАЩИТОЙ' if use_lock else 'БЕЗ ЗАЩИТЫ'} ---")

    threads = []
    # Запускаем 10 потоков, каждый делает 100 000 операций
    for i in range(10):
        t = threading.Thread(target=deposit, args=(100_000, use_lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  # Ждем завершения

    expected = 1_000_000
    print(f"Ожидали: {expected}")
    print(f"Получили: {bank_account}")
    print(f"Разница: {expected - bank_account}")


if __name__ == "__main__":
    run_test(use_lock=False)  # Скорее всего потеряет деньги
    print("-" * 20)
    run_test(use_lock=True)  # Будет ровно 1 000 000