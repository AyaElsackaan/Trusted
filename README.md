# Trusted
A secure network providing confidentiality and data integrity.

![img1](https://github.com/AyaElsackaan/Trusted/blob/main/diagrams/netw.JPG "img1")
## Implemented Algorithms:
### Confidentiality:
Data Encryption Standard (DES) using the following block cipher modes:
1. Electronic Codebook (ECB).
2. Cipher Block Chaining (CBC).
3. Cipher Feedback (CFB).
4. Counter (CTR).
### Data Integrity:
Hash-based Message Authentication Code (HMAC).

![img2](https://github.com/AyaElsackaan/Trusted/blob/main/diagrams/hamc.JPG "img2")

Hashing is implemented using RSA's MD5 message digest from python's hashlib. Find its documentation [here.](https://docs.python.org/3/library/hashlib.html)
## To run this code use:
```sh
python sender.py
Python receiver .py 
```
In two separate terminals simultaneously.
## Security Configurations:
You can choose the mode of operation only once at the start of the session.

Each session uses the same configurations, stored at “config.txt”.

To change the configurations or the mode of operation press Ctrl+C to end the current session and start a new session.

## Credits:
** Diagrams credits to William Stallings, _Cryptography and Network Security_, fifth edition.
