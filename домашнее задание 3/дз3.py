# python_tasks.py

import random
import string
from collections import Counter


def task1():
    print("\n=== Задание 1: Конвертер типов данных ===")
    try:
        num_str = input("Введите число: ").strip()
        if not num_str:
            print("Ошибка: пустой ввод")
            return
    except:
        print("Ошибка ввода")
        return

    try:
        num_int = int(num_str)
    except ValueError:
        try:
            num_int = int(float(num_str))
        except:
            print("Ошибка: невозможно преобразовать в целое число")
            return

    try:
        num_float = float(num_str)
    except ValueError:
        print("Ошибка: невозможно преобразовать в дробное число")
        return

    try:
        num_complex = complex(num_float)
    except:
        num_complex = complex(0)

    none_val = None
    is_even = (num_int % 2 == 0)

    data_dict = {
        'str': num_str,
        'int': num_int,
        'float': num_float,
        'complex': num_complex,
        'NoneType': none_val,
        'bool': is_even
    }

    print(f"Типы данных:\n"
          f"str: {data_dict['str']!r} ({type(data_dict['str']).__name__})\n"
          f"int: {data_dict['int']} ({type(data_dict['int']).__name__})\n"
          f"float: {data_dict['float']} ({type(data_dict['float']).__name__})\n"
          f"complex: {data_dict['complex']} ({type(data_dict['complex']).__name__})\n"
          f"NoneType: {data_dict['NoneType']} ({type(data_dict['NoneType']).__name__})\n"
          f"bool (чётное?): {data_dict['bool']} ({type(data_dict['bool']).__name__})")


def task2():
    print("\n=== Задание 2: Шифрование строки ===")
    text = input("Введите строку: ").strip()

    if not text:
        print("Введена пустая строка!")
        return

    try:
        encoded = text.encode('utf-8')
        decoded = encoded.decode('utf-8')
    except UnicodeError as e:
        print(f"Ошибка кодирования/декодирования: {e}")
        return

    new_text = ("Преобразовано: " + decoded).upper().replace(" ", "_")

    unique_chars = set(text)
    frozen_chars = frozenset(text)

    print(f"Оригинал: {text!r}\n"
          f"Закодировано: {encoded}\n"
          f"Декодировано: {decoded!r}\n"
          f"Новая строка: {new_text!r}\n"
          f"Уникальные символы (set): {unique_chars} (длина: {len(unique_chars)})\n"
          f"Замороженное множество: {frozen_chars}")


def task3():
    print("\n=== Задание 3: Анализатор чисел ===")
    nums_input = input("Введите числа через пробел: ").strip()

    if not nums_input:
        print("Ошибка: пустой ввод")
        return

    try:
        numbers = [float(x) for x in nums_input.split()]
    except ValueError:
        print("Ошибка: введите только числа, разделенные пробелами")
        return

    nums_tuple = tuple(numbers)
    total = sum(nums_tuple)
    is_sum_even = (int(total) % 2 == 0)

    unique_nums = set(numbers)
    types_dict = {num: type(num).__name__ for num in numbers}

    print(f"Список: {numbers}\n"
          f"Кортеж: {nums_tuple}\n"
          f"Сумма: {total} → чётная? {is_sum_even}\n"
          f"Уникальные числа: {unique_nums} (всего: {len(unique_nums)})\n"
          f"Типы чисел: {types_dict}")


def task4():
    print("\n=== Задание 4: Словарь уникальных слов ===")
    words_input = input("Введите слова через пробел: ").strip()

    if not words_input:
        print("Ошибка: пустой ввод")
        return

    word_list = words_input.lower().split()
    unique_words = {word for word in word_list}
    lengths_dict = {word: len(word) for word in unique_words}

    total_len = len(words_input)
    print(f"Исходная строка: '{words_input}' (длина: {total_len})\n"
          f"Уникальные слова: {unique_words} (всего: {len(unique_words)})\n"
          f"Длины слов: {lengths_dict}")


def task5():
    print("\n=== Задание 5: Генератор паролей ===")
    try:
        length_input = input("Введите длину пароля: ").strip()
        if not length_input:
            print("Используем длину 8 по умолчанию.")
            length = 8
        else:
            length = int(length_input)
            if length <= 0:
                print("Длина должна быть положительной. Используем 8.")
                length = 8
    except ValueError:
        print("Некорректная длина. Используем 8 по умолчанию.")
        length = 8

    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    if length > len(chars):
        print(f"Внимание: длина пароля ({length}) превышает количество уникальных символов ({len(chars)})")

    password = ''.join(random.choices(chars, k=length))

    char_set = set(password)
    frozen_char_set = frozenset(password)
    char_counter = Counter(password)
    counter_dict = {char: count for char, count in char_counter.items()}

    print(f"Сгенерированный пароль: {password}\n"
          f"Уникальные символы: {char_set} (всего: {len(char_set)})\n"
          f"Замороженное множество: {frozen_char_set}\n"
          f"Частота символов: {counter_dict}")


def task6():
    print("\n=== Задание 6: Анализатор множеств ===")
    list1_str = input("Введите первые числа через пробел: ").strip()
    list2_str = input("Введите вторые числа через пробел: ").strip()

    if not list1_str or not list2_str:
        print("Ошибка: один или оба ввода пустые")
        return

    try:
        list1 = [int(x) for x in list1_str.split()]
        list2 = [int(x) for x in list2_str.split()]
    except ValueError:
        print("Ошибка: введите только целые числа, разделенные пробелами")
        return

    set1 = set(list1)
    set2 = set(list2)

    # Безопасное удаление нуля
    set1.discard(0)

    intersection = frozenset(set1 & set2)

    print(f"Множество 1: {set1}\n"
          f"Множество 2: {set2}\n"
          f"Пересечение (frozenset): {intersection}\n"
          f"Размер пересечения: {len(intersection)}")


def task7():
    print("\n=== Задание 7: Словарь преобразований ===")
    nums_str = input("Введите числа через запятую: ").strip()

    if not nums_str:
        print("Ошибка: пустой ввод")
        return

    try:
        num_list = [float(x.strip()) for x in nums_str.split(',')]
    except ValueError:
        print("Ошибка: введите только числа, разделенные запятыми")
        return

    num_tuple = tuple(num_list)
    squares_dict = {num: num ** 2 for num in num_list}

    # Кодируем строку чисел
    numbers_str = ', '.join(str(num) for num in num_list)
    bytes_data = numbers_str.encode('utf-8')
    unique_bytes = set(bytes_data)

    print(f"Числа: {num_list}\n"
          f"Кортеж: {num_tuple}\n"
          f"Квадраты: {squares_dict}\n"
          f"Байты строки чисел: {bytes_data}\n"
          f"Уникальные байты: {unique_bytes} (всего: {len(unique_bytes)})")


def task8():
    print("\n=== Задание 8: Подсчёт символов ===")
    text = input("Введите строку: ").strip()

    if not text:
        print("Введена пустая строка!")
        return

    char_counter = Counter(text)
    unique_chars = set(text)
    frozen_unique = frozenset(text)
    ascii_dict = {char: ord(char) for char in unique_chars}

    print(f"Строка: {text!r} (длина: {len(text)})\n"
          f"Подсчёт символов: {dict(char_counter)}\n"
          f"Уникальные символы: {unique_chars}\n"
          f"Замороженные: {frozen_unique}\n"
          f"ASCII-коды: {ascii_dict}")


def task9():
    print("\n=== Задание 9: Анализатор кортежей ===")
    nums_str = input("Введите числа через пробел: ").strip()

    if not nums_str:
        print("Ошибка: пустой ввод")
        return

    try:
        numbers = [float(x) for x in nums_str.split()]
    except ValueError:
        print("Ошибка: введите только числа, разделенные пробелами")
        return

    nums_tuple = tuple(numbers)
    unique_nums = set(nums_tuple)
    other_set = {1.0, 2.0, 3.0}
    frozen_intersection = frozenset(unique_nums & other_set)
    types_dict = {num: type(num).__name__ for num in nums_tuple}

    print(f"Кортеж: {nums_tuple}\n"
          f"Уникальные числа: {unique_nums} (всего: {len(unique_nums)})\n"
          f"Пересечение с {{1.0, 2.0, 3.0}}: {frozen_intersection}\n"
          f"Типы: {types_dict}")


def task10():
    print("\n=== Задание 10: Менеджер контактов ===")
    contacts_input = input("Введите контакты (имя:номер; ...): ").strip()

    if not contacts_input:
        print("Ошибка: пустой ввод")
        return

    pairs = []
    for pair in contacts_input.split(';'):
        if pair.strip():
            if ':' not in pair:
                print(f"Ошибка: отсутствует ':' в '{pair}'")
                continue
            name_num = pair.strip().split(':', 1)
            if len(name_num) != 2:
                print(f"Ошибка: некорректный формат в '{pair}'")
                continue
            pairs.append((name_num[0].strip(), name_num[1].strip()))

    if not pairs:
        print("Не удалось извлечь ни одного контакта")
        return

    contact_tuples = pairs
    contacts_dict = {name: number for name, number in contact_tuples}
    names_set = {name for name, _ in contact_tuples}
    name_lengths = Counter(len(name) for name in names_set)
    frozen_numbers = frozenset(number for _, number in contact_tuples)

    print(f"Контакты (словарь): {contacts_dict}\n"
          f"Уникальные имена: {names_set}\n"
          f"Длины имён (частота): {dict(name_lengths)}\n"
          f"Номера (frozenset): {frozen_numbers}")


def main():
    tasks = {
        '1': task1,
        '2': task2,
        '3': task3,
        '4': task4,
        '5': task5,
        '6': task6,
        '7': task7,
        '8': task8,
        '9': task9,
        '10': task10,
        '0': lambda: print("Выход...") or exit(0)
    }

    while True:
        print("\n" + "="*50)
        print("Выберите задание (1–10) или 0 для выхода:")
        choice = input("Ваш выбор: ").strip()

        if choice in tasks:
            try:
                tasks[choice]()
            except KeyboardInterrupt:
                print("\n\nОперация прервана пользователем")
            except Exception as e:
                print(f"\nПроизошла ошибка: {e}")
                print("Возвращаемся в меню...")
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма завершена.")