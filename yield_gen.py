yield_gen

def simple_generator():
    print("Старт")
    yield 1 # функция замерла и вернула 1
    print("Продолжаем")
    yield 2 # снова умерла
    print("Финиш")

gen = simple_generator()
print(next(gen))
print(next(gen))



def worker():
    print("Рабочий готов")
    while True:
        item = yield #функция ждет пока в нее что-то пришлют
        print(f"Рабочий обработал: {item}")

w = worker()
next(w)

w.send("Кирпич")
w.send("Доска")



def sub_gen():
    yield "Данные 1"
    yield "Данные 2"
    return "Готово"

def main_gen():
    print("Делегируем работу")
    result = yield from sub_gen()
    print(f"Подчиненный вернул: {result}")

for x in main_gen():
    print(f"Получил: {x}")