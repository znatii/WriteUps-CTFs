#!/usr/bin/python3
import os

from sympy import solve

flag = bytes.fromhex("134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9")
class XOR:
    def __init__(self):
        self.key = os.urandom(4)
    def encrypt(self, data: bytes) -> bytes:
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored

    def solve(self, data: bytes) -> bytes:
        keyFinal = b''
        keyFinal += bytes(c ^ k for c,k in zip(data[:4],b"HTB{"))
        print(keyFinal)
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ keyFinal[i % len(keyFinal)]])
        return xored


    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)

def main():
    global flag
    crypto = XOR()
    print ('Flag:', crypto.solve(flag))

if __name__ == '__main__':
    main()
