class Starship:
    def __init__(self, name: str, shields: int = 100, hull: int = 100, energy: int = 100):
        self.name = name
        self.__shields = shields
        self.__hull = hull
        self.__energy = energy

    def take_damage(self, amount: int) -> None:
        """Нанесение урона кораблю"""
        if amount <= 0:
            print("Урон должен быть положительным числом!")
            return

        #Сначала урон поглощается щитами
        if self.__shields > 0:
            # Урон не может быть отрицательным
            damage_to_shields = min(amount, self.__shields)
            self.__shields -= damage_to_shields
            amount -= damage_to_shields
            print(f"Щиты поглотили {damage_to_shields} урона. Осталось щитов: {self.__shields}%")

        #Если урон остался и щиты пробиты, урон идёт в корпус
        if amount > 0 and self.__shields == 0:
            if self.__hull > 0:
                damage_to_hull = min(amount, self.__hull)
                self.__hull -= damage_to_hull
                print(f"Корпус получил {damage_to_hull} урона. Осталось прочности: {self.__hull}%")

            #Проверка на уничтожение корабля
            if self.__hull <= 0:
                self.__hull = 0
                print("Корабль уничтожен!")

    def recharge_shields(self, amount: int) -> None:
        """Восстановление щитов с затратой энергии"""
        if amount <= 0:
            print("Количество восстановления должно быть положительным!")
            return

        #Проверяем, есть ли энергия для восстановления
        energy_needed = amount // 2  # Предположим, что для восстановления 2% щитов нужна 1 единица энергии
        if energy_needed == 0 and amount > 0:
            energy_needed = 1

        if self.__energy < energy_needed:
            print(f"Недостаточно энергии! Нужно {energy_needed}, доступно {self.__energy}")
            return

        #Тратим энергию
        self.__energy -= energy_needed

        #Восстанавливаем щиты, но не более 100%
        old_shields = self.__shields
        self.__shields = min(100, self.__shields + amount)
        restored = self.__shields - old_shields

        print(f"Щиты восстановлены на {restored}%. Теперь щиты: {self.__shields}%")
        print(f"Затрачено энергии: {energy_needed}. Осталось энергии: {self.__energy}")

    def get_status(self) -> str:
        """Возвращает строку со статусом корабля"""
        status = f"Корабль '{self.name}': Щиты: {self.__shields}%, Корпус: {self.__hull}%, Энергия: {self.__energy}%"
        if self.__hull <= 0:
            status += " (УНИЧТОЖЕН)"
        elif self.__shields <= 0:
            status += " (Щиты пробиты)"
        return status

    #Геттеры для атрибутов (опционально, для удобства)
    def get_shields(self) -> int:
        return self.__shields

    def get_hull(self) -> int:
        return self.__hull

    def get_energy(self) -> int:
        return self.__energy

    def add_energy(self, amount: int) -> None:
        """Метод для добавления энергии (например, от солнечных батарей)"""
        if amount > 0:
            self.__energy = min(100, self.__energy + amount)
            print(f"Добавлено {amount}% энергии. Теперь энергии: {self.__energy}%")


#Демонстрация работы класса
if __name__ == "__main__":
    print("=== Тестирование звездолета 'Галактика' ===")
    ship = Starship("Галактика")

    print("\n1. Начальный статус:")
    print(ship.get_status())

    print("\n2. Получаем урон 70:")
    ship.take_damage(70)
    print(ship.get_status())

    print("\n3. Получаем урон 40 (щиты должны закончиться):")
    ship.take_damage(40)
    print(ship.get_status())

    print("\n4. Восстанавливаем щиты на 50:")
    ship.recharge_shields(50)
    print(ship.get_status())

    print("\n5. Получаем урон 120 (пробиваем щиты и повреждаем корпус):")
    ship.take_damage(120)
    print(ship.get_status())

    print("\n6. Добавляем энергию и восстанавливаем щиты:")
    ship.add_energy(50)
    ship.recharge_shields(80)
    print(ship.get_status())

    print("\n7. Получаем смертельный урон 150:")
    ship.take_damage(150)
    print(ship.get_status())

    print("\n=== Тестирование завершено ===")