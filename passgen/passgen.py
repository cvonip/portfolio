import random

print('Your Password: ')

chars='qwertyuiopasdfghjklzxcvbnm,1234567890!@#$%^&*()'

password=''
for x in range(16):
    password+= random.choice(chars)

print(password)
