#Зеленая стадия
# def is_valid_password(pwd):
#     #Проверка длины
#     if len(pwd) < 8:
#         return False
#
#     #Проверка на цифру
#     has_number = False
#     for char in pwd:
#         if char.isdigit():
#             has_number = True
#             break
#
#     if not has_number:
#         return False
#
#     return True


#Синяя стадия (Рефакторинг)
def is_valid_password(pwd):
    has_length = len(pwd) >= 8
    has_digit = any(char.isdigit() for char in pwd)

    return has_digit and has_length