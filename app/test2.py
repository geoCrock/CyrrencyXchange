import redis

# Подключение к Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Имя списка
key_name = 'mylist'
r.delete(key_name)
# Список элементов для добавления
items = ['apple', 'banana', 'orange']

# Добавление элементов в конец списка
r.rpush(key_name, *items)
# Добавление элементов в начало списка
# r.lpush(key_name, *items)

# Получение всех элементов списка
list_values = r.lrange(key_name, 0, -1)
print("Список в Redis:", list_values)
