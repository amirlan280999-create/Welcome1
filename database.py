#RAW SQL
# sql = "SELECT * FROM users WHERE age>18;"
# # cursor.execute(sql)
# # rows = cursor.fetchall()

#Объектный подход с ORM
# users = User.objects.filter(age__gt=18)
#
# for user in users:
#     print(user.name)

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    #1 Имя таблицы
    __tablename__ = "users"

    #2 Колонки
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    #3 Связь
    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)

    #4. Внешний ключ (физическая связь)
    owner_id = Column(Integer, ForeignKey("users.id"))

    #5. Обратная связь
    #Позволяет получить объект юзера через post.owner
    owner = relationship("User", back_populates="posts")

#без back_populates
# new_post.owner = petya
# petya.posts.append(new_post)

#c back_populates
# new_post.owner = petya