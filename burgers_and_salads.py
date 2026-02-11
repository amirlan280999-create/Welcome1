import time
import threading
import random
from concurrent.futures import ThreadPoolExecutor

class Grill:
    def __init__(self, capacity=2):
        self.capacity = capacity
        #семафор - это счетчик ключей
        #если capacity=2 то только 2 потока могут войти в блок with
        #Остальные будут ждать в очереди
        self.sem = threading.Semaphore(capacity)

    def fry_patty(self, chef_name):
        """Жарит котлету. Это I/O операция (ждем нагрева)"""
        print(f"      {chef_name} ждет свободное место на гриле")

        with self.sem:
            print(f"     {chef_name} положил котлету! (Занято мест): {self.capacity - self.sem._value}")

            coocing_time = random.uniform(1.5, 2.5)
            time.sleep(coocing_time)

            print(f"    {chef_name} снял сочную котлету")


class Customer:
    def __init__(self, name, order_item):
        self.name = name
        self.order_item = order_item

    def __repr__(self):
        return f"Клиент {self.name}"


def process_order(customer, grill):
    chef_name = threading.current_thread().name

    print(f"{chef_name} принял заказ от {customer.name}: {customer.order_item}")

    #1. Подготовка булочки
    time.sleep(0.5)

    #2. Жарка котлеты, повар идет к общему гриллю
    # конкурентность
    grill.fry_patty(chef_name)

    #cборка бургера
    time.sleep(0.5)

    print(f" {chef_name} отдал заказ {customer.name}!")
    return f"Заказ для {customer.name} выполнен!"


if __name__ == "__main__":
    #создаем оборудованеие
    my_grill = Grill(capacity=2)

    #создаем очередь клиентов
    customers = [
        Customer("Петя", "Чизбургер"),
        Customer("Вася", "БигМак"),
        Customer("Мария", "Гамбургер"),
        Customer("Саша", "Чикенбургер"),
        Customer("Акакий", "Двойной"),
        Customer("Борис", "Четвертьфунтовый с сыром"),
    ]


    # нанимаем поваров
    with ThreadPoolExecutor(max_workers=3, thread_name_prefix="Повар") as executor:
        #отправляем клиентов в обработку
        futures = [executor.submit(process_order, client, my_grill) for client in customers]

        for f in futures:
            f.result()

    print("Смена закончена")