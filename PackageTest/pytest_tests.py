#Обычный питоновский assert
#assert a == b

#фикстуры
#@pytest.fixture


import pytest

#1 этап
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.items.append({"name": name, "price": price})

    def get_total(self):
        return sum(item["price"] for item in self.items)

#2 этап

#фикстуры (подготовки данных)
#Эта фикстура создает пустую корзину
@pytest.fixture
def empy_cart():
    print("\n[Фикстура] Создаю пустую корзину...")
    return Cart()

#Эта фикстура использует предыдущую фикстуру
@pytest.fixture
def cart_with_items(empy_cart):
    print("\n[Фикстура] Наполняю корзину товарами")
    empy_cart.add_item("Яблоко", 100)
    empy_cart.add_item("Банан", 150)
    return empy_cart


#3 этап
#Тест просит пустую корзину
def test_add_item(empy_cart):
    empy_cart.add_item("Апельсин", 200)

    assert len(empy_cart.items) == 1
    assert empy_cart.get_total() == 200

#Тест просит уже наполненную корзину
def test_total_calculation(cart_with_items):
    assert cart_with_items.get_total() == 250


#Тестируем ошибку (Аналог assertRaises из unittest)
def test_negative_price(empy_cart):
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        empy_cart.add_item("Неправильный объект", -500)



#Параметризация (запуск одного теста с разными данными)

#декоратор запускает этот тест 3 раза с разными значениями и ожидаемой суммой
@pytest.mark.parametrize("price, expected_total", [
    (0, 0), #бесплатный товар
    (99.99, 99.99), #дробная цена
    (5000, 5000) #дорогой товар
])
def test_various_prices(empy_cart, price, expected_total):
    empy_cart.add_item("Предмет", price)
    assert empy_cart.get_total() == expected_total
