import random
import hashlib
import copy
import ast
from mnemonic import Mnemonic
#prenom = input('Entrez votre prénom (entre guillemets) : ')
#print('Bonjour,', prenom)

# print("--------------------------------------")
#t = random.randint(0, 8)
# print(t)
#b = bin(t)
# print(b)
# print(len(b))
# print("--------------------------------------")
# len(b)
x = random.randint(0, 340282366920938500000000000000000000000)
print(x)

bin = bin(x)
print(type(bin))
print(bin)
print(len(bin))
print(format(x, '0128b'))
print(type(format(x, '0128b')))
print(len(format(x, '0128b')))

seed = format(x, '0128b')

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


# print(number)
# print(type(number))

# intnumber = copy.copy(number)
# intnumber = int(intnumber)
# print(type(intnumber))
# checksum = bin(x)


# checksumquartebit = format(checksum, '04b')
# print(checksumquartebit)
# print(len(checksumquartebit))

if number == "0":
    checksum = "0000"
if number == "1":
    checksum = "0001"
if number == "2":
    checksum = "0010"
if number == "3":
    checksum = "0011"
if number == "4":
    checksum = "0100"
if number == "5":
    checksum = "0101"
if number == "6":
    checksum = "0110"
if number == "7":
    checksum = "0111"
if number == "8":
    checksum = "1000"
if number == "9":
    checksum = "1001"


seedun = seed[0:11]
print(len(seedun))
seeddeux = seed[11:22]
seedtrois = seed[22:33]
seedquatre = seed[33:44]
seedcinq = seed[44:55]
seedsix = seed[55:66]
seedsept = seed[66:77]
seedhuit = seed[77:88]
seedneuf = seed[88:99]
seeddix = seed[99:110]
seedonze = seed[110:121]
seeddouze = seed[121:129] + checksum

print("------------seeddouze")
print(seeddouze)
print(len(seeddouze))

liste = []
with open("mnemonic_list.txt") as fichier:
    liste = fichier.read().split("\n")
print(len(liste))
print(seedun)
motun = liste[int(seedun, 2)-1]
motdeux = liste[int(seeddeux, 2)-1]
mottrois = liste[int(seedtrois, 2)-1]
motquatre = liste[int(seedquatre, 2)-1]
motcinq = liste[int(seedcinq, 2)-1]
motsix = liste[int(seedsix, 2)-1]
motsept = liste[int(seedsept, 2)-1]
mothuit = liste[int(seedhuit, 2)-1]
motneuf = liste[int(seedneuf, 2)-1]
motdix = liste[int(seeddix, 2)-1]
motonze = liste[int(seedonze, 2)-1]
motdouze = liste[int(seeddouze, 2)-1]
motmnemonictot = motun+" "+motdeux+" "+mottrois+" "+motquatre+" "+motcinq+" "+motsix + \
    " "+motsept+" "+mothuit+" " + \
    motneuf+" "+motdix+" "+motonze+" "+motdouze
print(motmnemonictot)
mnemo = Mnemonic("english")
seed = mnemo.to_seed(motmnemonictot, passphrase="")
print(seed)
##entropy = mnemo.to_entropy(motmnemonictot)
# print(entropy)


print("--------------------------------------")
