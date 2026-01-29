# Голосовое меню банка (IVR) (Ветвления)
import time

def bank_ivr_system():
    client_name = "Амирлан Хасаев"
    client_balance = 10000
    client_status = "VIP"

    print(f"Добро пожаловать в банк 'Финансовое Будущее'!")
    print(f"Здравствуйте, {client_name}!")
    print(f"[Статус: {client_status}]")
    print("=" * 50)

    call_active = True
    while call_active:
        print("\n[ГЛАВНОЕ МЕНЮ] Выберите опцию:")
        print("1. Проверить баланс счета")
        print("2. Управление картами")
        print("3. Соединение с оператором")
        print("0. Завершить звонок")
        print("(VIP: можете сказать 'перевод' для быстрого доступа)")

        try:
            choice = input("\nВведите номер опции или команду: ").strip().lower()
            print("-" * 40)

            if choice == "1":
                print(f"[БАЛАНС] Текущий баланс: {client_balance:.2f} BYN.")
                time.sleep(1)
                continue

            elif choice == "2":
                print("[КАРТЫ] Вы вошли в раздел управления картами")

                cards_active = True
                while cards_active:
                    print("\n   [МЕНЮ КАРТ]:")
                    print("   1. Блокировка карты")
                    print("   2. Заказ перевыпуска карты")
                    print("   9. Вернуться в главное меню")

                    cards_choice = input("   Ваш выбор: ").strip()

                    if cards_choice == "1":
                        print("   [БЛОКИРОВКА] Карта заблокирована.")
                        time.sleep(1)
                    elif cards_choice == "2":
                        print("   [ПЕРЕВЫПУСК] Запрос на перевыпуск отправлен.")
                        time.sleep(1)
                    elif cards_choice == "9":
                        print("   Возврат в главное меню...")
                        cards_active = False
                    else:
                        print("   Неверный выбор")

                continue

            elif choice == "3":
                print("[ОПЕРАТОР] Соединяю с оператором...")
                time.sleep(1)

                print("[ОПЕРАТОР] Ало! Здравствуйте! Чем могу помочь?")

                conversation_active = True
                while conversation_active:
                    talk = input("\n   [Вы говорите] (или 'выход' для завершения): ").strip().lower()

                    if talk == "выход":
                        print("   [ОПЕРАТОР] Спасибо за обращение! До свидания!")
                        conversation_active = False
                    elif "тариф" in talk:
                        print("   [ОПЕРАТОР] У нас есть Базовый, Премиум и VIP тарифы")
                    elif "график" in talk or "время" in talk:
                        print("   [ОПЕРАТОР] Отделения работают с 9:00 до 20:00")
                    elif talk == "":
                        print("   [ОПЕРАТОР] Вы всё ещё на связи?")
                    else:
                        print(f"   [ОПЕРАТОР] По вопросу '{talk}' нужна дополнительная информация")

                call_active = False
                break

            elif choice == "0":
                print("[СИСТЕМА] Завершение звонка...")
                call_active = False
                break

            elif choice == "перевод":
                if client_status == "VIP":
                    print("\n" + "="*50)
                    print("[VIP СЕРВИС] Обнаружена VIP команда 'перевод'!")
                    print("[VIP СЕРВИС] Соединяю с вашим персональным менеджером...")
                    print("="*50)

                    time.sleep(1)

                    manager_active = True
                    while manager_active:
                        print("\n   [ПЕРСОНАЛЬНЫЙ МЕНЕДЖЕР Мария]:")
                        print("   Амирлан, Добрый день! Я ваш персональный менеджер.")
                        print("   1. Быстрый перевод между своими счетами")
                        print("   2. Перевод другому клиенту нашего банка")
                        print("   3. Перевод в другой банк")
                        print("   9. Вернуться в главное меню")

                        transfer_choice = input("\n   Что нужно сделать? [1-3 или 9]: ").strip()

                        if transfer_choice == "1":
                            print("   [МЕНЕДЖЕР] Перевод между вашими счетами выполнен!")
                            print(f"   [МЕНЕДЖЕР] Комиссия: 0 руб. (VIP клиент)")
                            time.sleep(1)
                        elif transfer_choice == "2":
                            account = input("   [МЕНЕДЖЕР] Введите номер счета получателя: ")
                            amount = input("   [МЕНЕДЖЕР] Введите сумму перевода: ")
                            print(f"   [МЕНЕДЖЕР] Перевод {amount} руб. на счет {account} выполнен!")
                            print(f"   [МЕНЕДЖЕР] Комиссия: 0 руб. (VIP клиент)")
                            time.sleep(1)
                        elif transfer_choice == "3":
                            print("   [МЕНЕДЖЕР] Перевод в другой банк займет 1-2 рабочих дня")
                            time.sleep(1)
                        elif transfer_choice == "9":
                            print("   [МЕНЕДЖЕР] Возвращаю в главное меню...")
                            manager_active = False
                        else:
                            print("   [МЕНЕДЖЕР] Не поняла, повторите пожалуйста")

                    print("\n[СИСТЕМА] Возврат в главное меню...")
                    continue

                else:
                    print("\n[СИСТЕМА] Извините, команда 'перевод' доступна только для VIP клиентов.")
                    print("[СИСТЕМА] Ваш текущий статус: ", client_status)
                    print("[СИСТЕМА] Для переводов выберите опцию 3 (Оператор)")
                    time.sleep(2)
                    continue

            else:
                print("[ОШИБКА] Неверная опция. Выберите 1, 2, 3 или 0.")
                print("[ПОДСКАЗКА] VIP клиенты могут использовать команду 'перевод'")
                continue

        except KeyboardInterrupt:
            print("\n[СИСТЕМА] Звонок прерван.")
            break

    print("\n" + "="*50)
    print("[СИСТЕМА] Сеанс завершен. До свидания!")
    print("="*50)

if __name__ == "__main__":
    bank_ivr_system()



# main()
# ├── while call_active:                    # Основной цикл звонка
# │   ├── Вывод главного меню
# │   ├── Ввод пользователя
# │   ├── if choice == "1":                # Баланс
# │   │   └── continue → назад в while
# │   ├── elif choice == "2":              # Карты
# │   │   └── while cards_active:          # Вложенный цикл
# │   │       ├── Подменю карт
# │   │       └── if choice == "9": break → выход из вложенного
# │   ├── elif choice == "3":              # Оператор
# │   │   └── while conversation_active:   # Еще один вложенный
# │   │       └── break → выход к...
# │   │   └── break → выход из основного while
# │   ├── elif choice == "перевод":        # Специальная команда
# │   │   └── if client_status == "VIP":   # Сложная проверка
# │   │       └── while manager_active:    # VIP меню
# │   │           └── continue → назад в основной while
# │   └── else → ошибка → continue
# └── Завершение программы