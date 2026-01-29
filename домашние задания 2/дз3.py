# ЗАДАНИЕ 3: "Угадай число" (While + If + Else)
import random

# 1. Компьютер загадывает число
secret = random.randrange(1, 100)
attempts = random.randrange(2, 3)

print(" ИГРА 'УГАДАЙ ЧИСЛО'")
print(f"Угадайте число от 1 до 100. У вас {attempts} попыток.")
print("-" * 30)

# 2. Используем цикл for для ограниченного количества попыток
for attempt in range(1, attempts + 1):
    print(f"\nПопытка {attempt} из {attempts}")

    # 3. Получаем ввод от пользователя с проверкой
    try:
        guess = int(input("Ваш вариант: "))
    except ValueError:
        print(" Ошибка! Введите целое число.")
        continue  # Эта попытка не засчитывается

    # 4. Проверяем угадал ли пользователь
    if guess == secret:
        print(f" Победа! Вы угадали число {secret}!")
        break  # Прерываем цикл при победе

    # 5-6. Даем подсказки
    elif guess < secret:
        print(" Мало!")
    else:  # guess > secret
        print(" Много!")

# 7. Блок else выполняется, если цикл завершился без break
else:
    print(f"\n ВЫ ПРОИГРАЛИ! Было загадано число: {secret}")

print("\nСпасибо за игру!")
