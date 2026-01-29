def task10():
    print("\n=== Задание 10: Менеджер контактов (русские имена + белорусские номера) ===")

    print("Пример ввода: Иван:+375291234567; Анна:+375441112233; Александр:+375336667788")
    print("Формат: Имя:Номер (разделитель - точка с запятой)")
    print("\nБелорусские форматы номеров:")
    print("  +37529XXXXXXX (МТС)")
    print("  +37533XXXXXXX (МТС)")
    print("  +37544XXXXXXX (A1)")
    print("  +37525XXXXXXX (life:)")

    contacts_input = input("\nВведите контакты (имя:номер; ...): ").strip()

    if not contacts_input:
        print("Ошибка: пустой ввод")
        return

    pairs = []

    # Разделяем по точке с запятой
    for pair in contacts_input.split(';'):
        pair = pair.strip()
        if not pair:
            continue

        if ':' not in pair:
            print(f"Пропущено: '{pair}' - отсутствует ':'")
            continue

        parts = pair.split(':', 1)
        if len(parts) != 2:
            print(f"Пропущено: '{pair}' - некорректный формат")
            continue

        name = parts[0].strip()
        number = parts[1].strip()

        # Проверяем имя (допускаем русские буквы, пробелы и дефисы)
        if not name:
            print(f"Пропущено: '{pair}' - имя пустое")
            continue

        # Проверяем номер телефона (белорусский формат)
        valid = False
        operator = "неизвестный"

        # Удаляем все пробелы, дефисы, скобки
        cleaned_number = number.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')

        # Проверяем форматы белорусских номеров
        if cleaned_number.startswith('+375'):
            if len(cleaned_number) == 13:  # +375291234567
                code = cleaned_number[4:6]  # Код оператора
                if code in ['29', '33', '44', '25', '17', '15', '16']:
                    valid = True
                    if code in ['29', '33']:
                        operator = "МТС"
                    elif code == '44':
                        operator = "A1"
                    elif code == '25':
                        operator = "life:"
                    elif code in ['17', '15', '16']:
                        operator = "Белтелеком (городские)"
                    else:
                        operator = f"код {code}"

        # Также принимаем короткие форматы
        elif cleaned_number.startswith('80'):
            if len(cleaned_number) == 11 and cleaned_number.startswith('80'):  # 80291234567
                code = cleaned_number[2:4]
                if code in ['29', '33', '44', '25', '17', '15', '16']:
                    cleaned_number = '+375' + cleaned_number[2:]  # Преобразуем в международный
                    valid = True
                    if code in ['29', '33']:
                        operator = "МТС"
                    elif code == '44':
                        operator = "A1"
                    elif code == '25':
                        operator = "life:"
                    elif code in ['17', '15', '16']:
                        operator = "Белтелеком (городские)"
                    else:
                        operator = f"код {code}"

        if not valid:
            print(f"Пропущено: '{name}' - номер '{number}' не соответствует белорусскому формату")
            print(f"  Ожидается: +37529XXXXXXX, +37544XXXXXXX и т.д.")
            continue

        # Форматируем номер для красивого отображения
        if cleaned_number.startswith('+375') and len(cleaned_number) == 13:
            formatted_number = f"+375 ({cleaned_number[4:6]}) {cleaned_number[6:9]}-{cleaned_number[9:11]}-{cleaned_number[11:]}"
        else:
            formatted_number = cleaned_number

        pairs.append((name, formatted_number, operator))

    if not pairs:
        print("Не удалось извлечь ни одного контакта")
        return

    print(f"\nУспешно загружено контактов: {len(pairs)}\n")

    # Создаем различные структуры данных
    contacts_dict = {name: number for name, number, operator in pairs}
    contacts_with_operator = {name: (number, operator) for name, number, operator in pairs}
    names_set = {name for name, _, _ in pairs}
    name_lengths = Counter(len(name) for name in names_set)

    # Разделяем номера по операторам
    operators_dict = {}
    for name, number, operator in pairs:
        if operator not in operators_dict:
            operators_dict[operator] = []
        operators_dict[operator].append((name, number))

    # Создаем frozenset номеров
    frozen_numbers = frozenset(number for _, number, _ in pairs)

    # Статистика по именам
    russian_stats = {
        "всего имён": len(names_set),
        "самое длинное имя": max(names_set, key=len) if names_set else "нет",
        "самое короткое имя": min(names_set, key=len) if names_set else "нет",
        "средняя длина имени": sum(len(name) for name in names_set) / len(names_set) if names_set else 0
    }

    # Статистика по операторам
    operator_stats = {operator: len(numbers) for operator, numbers in operators_dict.items()}

    # Выводим результаты
    print("КОНТАКТЫ:")
    for i, (name, number, operator) in enumerate(pairs, 1):
        print(f"  {i}. {name}: {number} ({operator})")

    print(f"\nСЛОВАРЬ КОНТАКТОВ (имя -> номер):")
    for name, number in contacts_dict.items():
        print(f"  {name}: {number}")

    print(f"\nУНИКАЛЬНЫЕ ИМЕНА ({len(names_set)}):")
    for name in sorted(names_set):
        print(f"  - {name}")

    print(f"\nРАСПРЕДЕЛЕНИЕ ДЛИН ИМЕН:")
    for length, count in sorted(name_lengths.items()):
        print(f"  {length} символов: {count} имя(ён)")

    print(f"\nРАСПРЕДЕЛЕНИЕ ПО ОПЕРАТОРАМ:")
    for operator, count in sorted(operator_stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {operator}: {count} номер(ов)")
        for name, number in operators_dict[operator]:
            print(f"    - {name}: {number}")

    print(f"\nЗАМОРОЖЕННОЕ МНОЖЕСТВО НОМЕРОВ (frozenset):")
    print(f"  {frozen_numbers}")
    print(f"  Всего уникальных номеров: {len(frozen_numbers)}")

    print(f"\nСТАТИСТИКА ПО ИМЕНАМ:")
    for key, value in russian_stats.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.1f}")
        else:
            print(f"  {key}: {value}")

    # Дополнительный анализ
    print(f"\nДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ:")

    # Поиск дубликатов имен (если есть одинаковые имена с разными номерами)
    name_counter = Counter(name for name, _, _ in pairs)
    duplicates = {name: count for name, count in name_counter.items() if count > 1}
    if duplicates:
        print(f"  Найдены повторяющиеся имена:")
        for name, count in duplicates.items():
            numbers = [number for n, number, _ in pairs if n == name]
            print(f"    {name} ({count} раз): {', '.join(numbers)}")
    else:
        print("  Повторяющихся имен не найдено")

    # Проверка на популярные русские имена
    popular_russian_names = ["Александр", "Алексей", "Анна", "Мария", "Дмитрий",
                             "Сергей", "Екатерина", "Иван", "Ольга", "Наталья"]
    found_popular = [name for name in names_set if name in popular_russian_names]
    if found_popular:
        print(f"  Найдены популярные русские имена: {', '.join(sorted(found_popular))}")
    else:
        print("  Популярных русских имен не найдено")

    # Анализ по регионам (по коду оператора)
    print(f"\nРЕГИОНАЛЬНЫЙ АНАЛИЗ (по кодам):")
    region_codes = {
        '29': 'Минск и область (МТС)',
        '33': 'Минск и область (МТС)',
        '44': 'A1',
        '25': 'life:',
        '17': 'Минск (городские)',
        '15': 'Гродно (городские)',
        '16': 'Брест (городские)'
    }

    region_stats = {}
    for _, number, _ in pairs:
        # Извлекаем код из номера
        for code in ['29', '33', '44', '25', '17', '15', '16']:
            if f"({code})" in number:
                region_name = region_codes.get(code, f"код {code}")
                if region_name not in region_stats:
                    region_stats[region_name] = 0
                region_stats[region_name] += 1
                break

    for region, count in sorted(region_stats.items()):
        print(f"  {region}: {count} номер(ов)")


def task10_simple():
    """Упрощенная версия 10-го задания (как было раньше, но с улучшениями)"""
    print("\n=== Задание 10: Менеджер контактов ===")
    print("Пример: Иван:+375291234567; Анна:+375441112233; Александр:+375336667788")

    contacts_input = input("Введите контакты (имя:номер; ...): ").strip()

    if not contacts_input:
        print("Ошибка: пустой ввод")
        return

    pairs = []
    for pair in contacts_input.split(';'):
        if pair.strip():
            if ':' not in pair:
                print(f"Пропущено: '{pair}' - отсутствует ':'")
                continue
            parts = pair.strip().split(':', 1)
            if len(parts) == 2:
                name = parts[0].strip()
                number = parts[1].strip()

                # Базовая проверка номера
                if number.startswith('+375') and len(number.replace(' ', '').replace('-', '')) >= 13:
                    pairs.append((name, number))
                else:
                    print(f"Пропущено: '{name}' - номер не соответствует белорусскому формату")

    if not pairs:
        print("Не удалось извлечь ни одного контакта")
        return

    contact_tuples = pairs
    contacts_dict = {name: number for name, number in contact_tuples}
    names_set = {name for name, _ in contact_tuples}
    name_lengths = Counter(len(name) for name in names_set)
    frozen_numbers = frozenset(number for _, number in contact_tuples)

    print(f"\nУспешно загружено: {len(pairs)} контактов")
    print(f"\nКОНТАКТЫ (словарь): {contacts_dict}")
    print(f"УНИКАЛЬНЫЕ ИМЕНА ({len(names_set)}): {names_set}")
    print(f"ДЛИНЫ ИМЕН (частота): {dict(name_lengths)}")
    print(f"НОМЕРА (frozenset, {len(frozen_numbers)}): {frozen_numbers}")

    # Дополнительная информация
    print(f"\nСТАТИСТИКА:")
    print(f"  Всего контактов: {len(pairs)}")
    print(f"  Уникальных имен: {len(names_set)}")
    print(f"  Уникальных номеров: {len(frozen_numbers)}")
    if len(pairs) > len(frozen_numbers):
        print(f"  Внимание: Есть дубликаты номеров: {len(pairs) - len(frozen_numbers)}")