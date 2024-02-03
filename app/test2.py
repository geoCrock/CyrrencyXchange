import redis

# Подключение к Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Добавление данных
r.set('mykey', 'Hello')

# Получение данных
value = r.get('mykey').decode('utf-8')
print(value)
