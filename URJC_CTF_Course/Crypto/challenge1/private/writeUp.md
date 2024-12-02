# Inaccesible

This is a simple challenge, there are several hashes that are no longer secure like MD5 or SHA1, the challenge consists of a hash and a zip with a password

If we analyze the hash we see that it is a SHA1.

![Screenshot from 2024-12-02 21-42-12.png](Screenshot%20from%202024-12-02%2021-42-12.png)

So with a tool like hashcat and a wordlist like rockyou we can brute force it.

```

hashcat -a 0 -m 100 hash.txt rockyou.txt

```
![Screenshot from 2024-12-02 21-43-42.png](Screenshot%20from%202024-12-02%2021-43-42.png)