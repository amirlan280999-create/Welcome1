#валидатор паролей
#Красная стадия (пишем тест)

#импортируем функцию которой еще не существует
from PackageTest.auth import is_valid_password

def test_password_lenght():
    #короткий пароль, должен вернуть False
    assert is_valid_password("1234567") == False
    #нормальный пароль должен вернуть True
    assert is_valid_password("12345678") == True


def test_password_has_number():
    #Длина нормальная, но цифр нет - ждем False
    assert is_valid_password("abcdefgh") == False
    #Длина нормальная и есть цифра - ждем True
    assert is_valid_password("abcdefg1") == True