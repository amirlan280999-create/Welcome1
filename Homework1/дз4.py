# Задание 4: "Финансовый отчет"

# 1. Исходный список расходов в долларах
expenses_usd = [10.50, 4.20, 100.0, 50.5]

# 2. Курс доллара
rate = 92

# 3. Создаем словарь с помощью генератора словарей
# Ключ - сумма в долларах, значение - целое число рублей
expenses_rub = {usd: int(usd * rate) for usd in expenses_usd}

# 4. Выводим итоговый словарь
print("Финансовый отчет:")
print(f"Исходные расходы в USD: {expenses_usd}")
print(f"Курс USD к RUB: {rate}")
print(f"Расходы в RUB (без копеек): {expenses_rub}")

# Это Python код!
expenses_usd = [10.50, 4.20, 100.0, 50.5]
rate = 92
expenses_rub = {usd: int(usd * rate) for usd in expenses_usd}
print(expenses_rub)