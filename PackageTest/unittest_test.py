import unittest

def calculate_price(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Скидка должна быть от 0 до 100")

    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

#Класс с тестами
class TestPriceCalculator(unittest.TestCase):

    #Метод setUp(подготовка)
    #Вызывается автоматом перед каждым тестом
    def setUp(self):
        self.standard_price = 1000

    #Тест 1 (успешный сценарий)
    def test_normal_discount(self):
        actual = calculate_price(self.standard_price, 20)

        self.assertEqual(actual, 800.0)


    def test_zero_discount(self):
        actual = calculate_price(self.standard_price, 0)
        self.assertEqual(actual, 1000.0)

    def test_invalid_discount_raises_error(self):
        with self.assertRaises(ValueError) as context:
            calculate_price(self.standard_price, 150)

        self.assertEqual(str(context.exception), "Скидка должна быть от 0 до 100")


if __name__ == "__main__":
    unittest.main()