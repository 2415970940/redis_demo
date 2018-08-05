import redis

client= redis.StrictRedis(host='127.0.0.1',port=6379)
key = 'hello'
setResult = client.set(key,"redis-python")
print(setResult)

value = client.get(key)
print(value)