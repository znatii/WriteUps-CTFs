from sage.all import *
from Crypto.PublicKey import RSA
from pwn import *

p = process('./server.py')
#p = remote('94.237.54.116',49633)

for i in range(5):
    p.readuntil(b'?\n')
    pk = p.readuntil(b'-----END PUBLIC KEY-----')
    print(pk)
    key = RSA.import_key(bytes(pk))
    n = key.n
    e = key.e

    p1,q1 = factor(n)
    p1 = str(p1[0])
    q1 = str(q1[0])

    p.sendlineafter('enter your first pumpkin = ', p1)
    p.sendlineafter('enter your second pumpkin = ', q1)
    sleep(1)

print (p.recvline())
print (p.recvline())
print (p.recvline())
print (p.recvline())
