from abc import ABC, abstractmethod

#Абстрактный класс Notification
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

#Реализация классов уведомлений
class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Отправляем письмо на почту: {message}")

class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Шлем СМС: {message}")

#Push-уведомление с ограничением длины
class PushNotification(Notification):
    MAX_LENGTH = 10

    def send(self, message: str) -> None:
        if len(message) > self.MAX_LENGTH:
            message = message[:self.MAX_LENGTH - 3] + "..."
        print(f"Пуш-уведомление: {message}")

#Создаём список пользователей (объектов разных типов уведомлений)
users_notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification(),
    EmailNotification(),
    PushNotification()
]

#Отправляем всем сообщение "Ваш заказ готов!"
for notification in users_notifications:
    notification.send("Ваш заказ готов!")