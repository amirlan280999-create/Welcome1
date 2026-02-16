import os
import sys  # Импорт есть, но он нигде не используется!

def calculate_salary(  base,bonus): # Ужасные пробелы
    total=base+bonus # Нет пробелов вокруг = и +
    return total

print( calculate_salary(100, 20) ) # Лишние пробелы внутри скобок