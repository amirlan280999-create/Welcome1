# Задание 1: "Шпионская радиограмма"

# Исходная шифровка, перехваченная у врагов
encrypted_message = "gnirob_si_gnidoc_tpyrc_eht"

print("=" * 50)
print("ШАГ 1: Разворачиваем всю строку задом наперед")
print("=" * 50)

# Враги писали слова задом наперед, поэтому разворачиваем всю строку
# Срез [::-1] означает: от начала до конца с шагом -1 (в обратном порядке)
normal_message = encrypted_message[::-1]
print(f"Исходная шифровка: {encrypted_message}")
print(f"После разворота:   {normal_message}")
print()

print("=" * 50)
print("ШАГ 2: Разделяем строку на отдельные слова")
print("=" * 50)

# Враги разделяли слова нижним подчеркиванием '_'
# Метод split('_') делит строку на части по указанному разделителю
words = normal_message.split('_')
print(f"Слова после разделения: {words}")
print(f"Всего слов: {len(words)}")
print()

print("=" * 50)
print("ШАГ 3: Извлекаем первое и последнее слово")
print("=" * 50)

# В Python индексы начинаются с 0
# words[0] - первый элемент списка (первое слово)
first_word = words[0]  # "the"
# words[-1] - последний элемент списка (последнее слово)
last_word = words[-1]  # "boring"

print(f"Первое слово (words[0]): '{first_word}'")
print(f"Последнее слово (words[-1]): '{last_word}'")
print()

print("=" * 50)
print("ШАГ 4: Собираем новую фразу")
print("=" * 50)

# Собираем фразу "The coding is boring"
# Метод capitalize() делает первую букву строки заглавной
phrase = first_word.capitalize() + " coding is " + last_word
print(f"Собрали фразу: {phrase}")
print()

print("=" * 50)
print("ШАГ 5: Заменяем 'boring' на 'cool'")
print("=" * 50)

# Метод replace() заменяет все вхождения подстроки
new_phrase = phrase.replace("boring", "cool")
print(f"До замены:    {phrase}")
print(f"После замены: {new_phrase}")
print()

print("=" * 50)
print("ШАГ 6: Преобразуем в верхний регистр (капс)")
print("=" * 50)

# Метод upper() преобразует все символы строки в верхний регистр
final_result = new_phrase.upper()
print(f"Итоговая строка: {final_result}")

print("\n" + "=" * 50)
print("КРАТКИЙ ИТОГ ВСЕХ ПРЕОБРАЗОВАНИЙ:")
print("=" * 50)
print(f"1. Было:      {encrypted_message}")
print(f"2. Развернули: {normal_message}")
print(f"3. Собрали:    {phrase}")
print(f"4. Заменили:   {new_phrase}")
print(f"5. Капс:       {final_result}")
print("=" * 50)