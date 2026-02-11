from database import SessionLocal, engine
from models import Base, User, Post

#1. Создаемп таблицы
#Эта команда смотрит на все классы, унаслед. от Base
#и создает для них таблицы в PostgreSQL
print("Создаем таблицы в БД...")
Base.metadata.create_all(bind=engine)


#2. Открываем сессию
db = SessionLocal()

try:
    #Шаг 1 создаем пользователя
    print("Создаем пользака")

    #создаем объект Python
    new_user = User(
        email = "petya@example.com",
        password = "password"
    )
    # Добавляем в список на сохранение
    db.add(new_user)

    #Фиксируем изменения
    db.commit()

    #Обновляем объект данными
    db.refresh(new_user)
    print(f"Пользователь создан! ID: {new_user.id}, email: {new_user.email}")

    #Шаг 2 Создаем посты

    #Способ №1 через объект (ORM стиль)
    post1 = Post(
        title = "Мой первый пост",
        body="Всем привет!!",
        owner=new_user
    )

    #Способ №2 через ID(SQL стиль)
    post2 = Post(
        title="Второй пост",
        body="Пишу через поле owner_id",
        owner_id=new_user.id #передаем число
    )

    #добавим оба поста в сессию
    db.add_all([post1, post2])

    #сохраняем (INSERT INTO)
    db.commit()

    print("Посты добавлены")

    #Шаг 3 Проверка (чтение)
    print(f"\nСписок постов пользователя {new_user.email}:")

    for post in new_user.posts:
        print(f"- {post.title} (ID поста: {post.id})")

finally:
    db.commit()