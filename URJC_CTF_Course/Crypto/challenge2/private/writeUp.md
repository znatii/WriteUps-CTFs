# Desenmascarados! (Unmasked!)

The challenge gives us a list of leaked passwords and an md5 hash.

There is a feature in tools like John the Ripper or Hashcat that allows bruteforcing a hash with a mask, if we know part of the content of the hash the possibilities are shortened
So let's apply it

```

hashcat -a 3 -m 0 hash.txt Alumno_?d?d?u

```

![Screenshot from 2024-12-02 21-57-43.png](Screenshot%20from%202024-12-02%2021-57-43.png)