import random as rn
import string as s

chars = list(s.digits + s.ascii_letters + '@#$')

length = int(input('Enter the length: '))
password =[]
for i in range(length):
    password.append(rn.choice(chars))
sh = rn.shuffle(password)
print(''.join(password))

