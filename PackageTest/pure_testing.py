def calculate_price(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Скидка должна быть от 0 до 100")

    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

#Начало тестов
def test_calculate_price_normal():
    #Подготовка
    price = 1000
    discount = 20
    expected = 800.0

    #Действие
    actual = calculate_price(price, discount)

    #Проверка
    assert actual == expected, f"Ожидали {expected}, получили {actual}"
    print("Тест пройден")

def test_calculate_price_zero_discount():
    #Подготовка
    price = 500
    discount = 0
    expected = 500.0

    #Действие
    actual = calculate_price(price, discount)

    #Проверка
    assert actual == expected, f"Скидка 0% не должна менять цену"
    print("Тест пройден")


def test_calculate_price_invalid_discont():
    #Подготовка
    price = 1000
    bad_discount = 1500


    #Действие вместе с проверкой
    try:
        calculate_price(price,bad_discount)

        assert False, "функция должна была выбросить ValueError, но промолчала"
    except ValueError as e:
    #Проверка
        assert str(e) ==  "Скидка Должна быть от 0 до 100", "Выброшена ошибка с неправильным значением"
        print("Тест пройден")


if __name__ == "__main__":
    print("Запуск тестов....")

    test_calculate_price_normal()
    test_calculate_price_zero_discount()
    test_calculate_price_invalid_discont()

    print("Все тесты прошли успешно!!!")