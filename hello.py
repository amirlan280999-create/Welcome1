import sys


#argv[0] - имя самого скрипта
#argv[1:] это то что передаем
if len(sys.argv) < 2:
    print("Ошибка! Используй: Python hello.py [ИМЯ]")
    sys.exit()

script_name = sys.argv[0]
user_name = sys.argv[1]

print()