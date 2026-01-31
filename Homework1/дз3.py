# 1. Даны два списка
my_music = ["Pop", "Rock", "Jazz", "Pop"]
friend_music = ["Rap", "House", "Rock", "Rap"]

# 2. Объединить без дублей (используя set)
all_genres = set(my_music) | set(friend_music)

# 3. Найти общие жанры
common = set(my_music) & set(friend_music)

# 4. Найти только у друга
only_friend = set(friend_music) - set(my_music)

# 5. Вывести количество уникальных
count = len(all_genres)

print("1. Все жанры:", all_genres)
print("2. Общие жанры:", common)
print("3. Только у друга:", only_friend)
print("4. Уникальных жанров:", count)
