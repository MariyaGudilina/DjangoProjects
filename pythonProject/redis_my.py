import redis

redis_database = redis.Redis(
    host='redis-16390.c89.us-east-1-3.ec2.cloud.redislabs.com',
    port=16390,
    password='IQLecTEJp8BJZGJhimoxUCGxu9Datp6j'

)

cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        redis_database.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = redis_database.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = redis_database.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break
