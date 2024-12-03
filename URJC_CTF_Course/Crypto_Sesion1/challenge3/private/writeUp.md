# Los apuntes de John Po'John (John Po'John's notes)

In this challenge we are only given a zip, we can try to crack the password with ziptojohn, the steps are the following.

we get the hash of the zip:

```

ziptojohn apuntes_CTF.zip > hash.txt

```

Then with john we can try to bruteforce the password:

```

john -w rockyou.txt hash.txt

```

Once we have the password we see that there is a txt with a very strange encryption, in the statement it mentions that "your brain explodes" so we try with the brain fuck encryption and it actually works

![Screenshot from 2024-12-02 22-18-01.png](Screenshot%20from%202024-12-02%2022-18-01.png)

Finally, we see that it seems that the letters do not match but the format does, it is seen that it is a rot13 and we get the flag.

![Screenshot from 2024-12-02 22-18-33.png](Screenshot%20from%202024-12-02%2022-18-33.png)