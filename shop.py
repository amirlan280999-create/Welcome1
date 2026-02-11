import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# ========== 1. НАСТРОЙКА ==========
DATABASE_URL = "postgresql://postgres:1234@localhost:5433/shop"
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# ========== 2. МОДЕЛИ ==========
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User(name='{self.name}')>"

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price})>"  # Исправлено

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    user = relationship("User", back_populates="orders")
    product = relationship("Product")

    def __repr__(self):
        return f"<Order(User: {self.user.name}, Item: {self.product.name})>"

# ========== 3. СОЗДАНИЕ ТАБЛИЦ ==========
Base.metadata.create_all(engine)

# ========== 4. БИЗНЕС-ЛОГИКА (CRUD) ==========

def create_initial_data():
    """C - Create (INSERT)"""
    if session.query(User).count() == 0:
        print("--- [C] НАПОЛНЯЕМ БАЗУ ---")

        u1 = User(name="Ivan")
        u2 = User(name="Maria")
        p1 = Product(name="iPhone 15", price=1000)
        p2 = Product(name="Samsung S24", price=900)
        p3 = Product(name="Чехол", price=20)

        session.add_all([u1, u2, p1, p2, p3])
        session.commit()
        print("Пользователи и товары созданы.")

def buy_product(user_name, product_name):
    """C - Create (Order)"""
    print(f"\n--- [C] НОВЫЙ ЗАКАЗ: {user_name} покупает {product_name} ---")

    user = session.query(User).filter(User.name == user_name).first()
    product = session.query(Product).filter(Product.name == product_name).first()

    if user and product:
        new_order = Order(user_id=user.id, product_id=product.id)
        session.add(new_order)
        session.commit()
        print(f"Успешно! Заказ №{new_order.id} создан.")
    else:
        print("Ошибка: Юзер или Товар не найден.")

def show_orders_by_user(user_name):
    """R - Read (SELECT + JOIN)"""
    print(f"\n--- [R] ИСТОРИЯ ЗАКАЗОВ: {user_name} ---")

    user = session.query(User).filter_by(name=user_name).first()
    if user:
        if user.orders:
            for order in user.orders:
                print(f"- Купил: {order.product.name} за {order.product.price}$")
        else:
            print("У пользователя нет заказов.")
    else:
        print("Пользователь не найден.")

def update_price(product_name, new_price):
    """U - Update"""
    print(f"\n--- [U] ИНФЛЯЦИЯ: Меняем цену на {product_name} ---")

    product = session.query(Product).filter_by(name=product_name).first()
    if product:
        old_price = product.price
        product.price = new_price
        session.commit()
        print(f"Цена изменена: {old_price} -> {new_price}")
    else:
        print("Товар не найден.")

def delete_order(order_id):
    """D - Delete"""
    print(f"\n--- [D] ОТМЕНА ЗАКАЗА №{order_id} ---")

    order = session.query(Order).filter_by(id=order_id).first()
    if order:
        session.delete(order)
        session.commit()
        print(f"Заказ №{order_id} удален.")
    else:
        print(f"Заказ №{order_id} не найден.")

def delete_all_orders():
    """D - Delete all orders"""
    print("\n--- [D] УДАЛЕНИЕ ВСЕХ ЗАКАЗОВ ---")
    count = session.query(Order).count()
    session.query(Order).delete()
    session.commit()
    print(f"Удалено {count} заказов.")

# ========== 5. ТЕСТИРОВАНИЕ ==========
if __name__ == "__main__":
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ SQLAlchemy CRUD")
    print("=" * 50)

    # Создаем начальные данные
    create_initial_data()

    # Покупаем товары
    buy_product("Ivan", "iPhone 15")
    buy_product("Maria", "Samsung S24")
    buy_product("Ivan", "Чехол")

    # Показываем заказы
    show_orders_by_user("Ivan")
    show_orders_by_user("Maria")

    # Обновляем цену
    update_price("iPhone 15", 950)

    # Удаляем заказ
    if session.query(Order).count() > 0:
        first_order = session.query(Order).first()
        delete_order(first_order.id)

    # Показываем финальное состояние
    print("\n--- ФИНАЛЬНОЕ СОСТОЯНИЕ ---")
    print(f"Пользователей: {session.query(User).count()}")
    print(f"Товаров: {session.query(Product).count()}")
    print(f"Заказов: {session.query(Order).count()}")

    # Закрываем сессию
    session.close()
    print("\nСессия закрыта.")