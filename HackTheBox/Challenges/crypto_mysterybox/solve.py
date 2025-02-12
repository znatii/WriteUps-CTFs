from pwn import *
import math
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes, isPrime, inverse
from functools import reduce

to_sign = bytes_to_long(b"Username: Admin, Access code: CryptoBestCategoryF3")


def calculateTosign(n, io):
    k = 2

    invK = inverse(k, n)
    m = (invK * to_sign) % n

    cm = get_signature(io, m)
    ck = get_signature(io, k)

    toSign_sign = (cm * ck) % n

    return toSign_sign


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_list(numbers):
    return reduce(lambda x, y: gcd(x, y), numbers)

def send_signature(io, signature):
    try:
        m = bytes_to_long(b"Username: Admin, Access code: CryptoBestCategoryF3")
        io.sendlineafter(b"Enter your option: ", b"2")
        m_hex = hex(m)[2:]
        if len(m_hex)%2 != 0:
            m_hex = "0" + m_hex
        io.sendlineafter(b"Enter your message in hex: ", m_hex)


        sig_hex = hex(signature)[2:]
        if len(sig_hex)%2 != 0:
            sig_hex = "0" + sig_hex
        io.sendlineafter(b"Enter your signature in hex: ", sig_hex)
        resp = io.recvline()
        return resp
    except:
        return None

def get_signature(io, m):
    try:
        io.sendlineafter(b"Enter your option: ", b"1")
        m_hex = hex(m)[2:]
        if len(m_hex)%2 != 0:
            m_hex = "0" + m_hex
        # Convert to hex without '0x' prefix
        io.sendlineafter(b"Enter your message to be signed in hex: ", m_hex)
        resp = io.recvline()
        print(resp)

        if b'You cannot sign' in resp:
            return None

        # Extract signature from response
        sig_str = resp.split()[-1].strip().decode()
        return int(sig_str)
    except:
        return None

def recover_n(host, port):
    #io = remote(host, port)
    io = process("./server.py")
    k_values = []

    # Message pairs to test
    test_pairs = [(2, 3), (2, 5), (3, 5), (2, 7)]

    for m1, m2 in test_pairs:
        c1 = get_signature(io, m1)
        if not c1: continue

        c2 = get_signature(io, m2)
        if not c2: continue

        m3 = m1 * m2
        c3 = get_signature(io, m3)
        if not c3: continue

        k = c1 * c2 - c3
        k_values.append(abs(k))  # Use absolute value

        # Early exit if we have enough values
        if len(k_values) >= 3:
            break

    if not k_values:
        print("Failed to collect any k values")
        return None

    n = gcd_list(k_values)

    print(n)

    signature = calculateTosign(n, io)

    flag = send_signature(io, signature)

    print(flag)

    io.close()

    # Verify n is not 1 (trivial GCD)
    if n == 1:
        print("GCD resulted in 1 - need more k values")
        return None

    return n

if __name__ == "__main__":
    target_ip = "83.136.253.1"  # Replace
    target_port = 46859       # Replace

    recovered_n = recover_n(target_ip, target_port)
    if recovered_n:
        print(f"Recovered modulus: {recovered_n}")
        print(f"Bit-length: {recovered_n.bit_length()}")
    else:
        print("Failed to recover modulus")