import random
import hashlib
import copy
import ast
from mnemonic import Mnemonic

x = random.randint(0, 340282366920938500000000000000000000000)
seed = format(x, '0128b')


bin = bin(x)
myseedencoded = seed.encode()

m = hashlib.sha256(myseedencoded)
myseedhash = m.hexdigest()
print("seeeeeeeeed")
print(myseedhash)

print("recherche chiffre")
i = 0
numberreturn = "a"
while numberreturn != True:
    numberreturn = myseedhash[i].isdigit()
    number = myseedhash[i]
    i += 1


print(number)

bin2 = bin(int(number))
print(bin2)
print(type(bin2))

checksumquartebit = format(bin2, '0128b')
print(checksumquartebit)
