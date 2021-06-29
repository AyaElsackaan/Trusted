# first of all import the socket library
import socket
from Mode_Operations import *
import random
import json
import os
import time
from Hashing import*
def genrate_key_randomly():
    key=""
    for i in range(64):
        key=key+str(random.randrange(0, 2))
    return key

f = open("config.txt", "w")
values = {}
hash_key = genrate_key_randomly()
values['hash_key'] = hash_key
# print(result_hash.digest_size)
mode_of_operation = input("Enter mode of operation: 1 ECB 2 CBC 3 CFB 4 CTR")
key = genrate_key_randomly()
values['key'] = key
values['mode'] = mode_of_operation
IV = genrate_key_randomly()
values['IV'] = IV
Counter = genrate_key_randomly()
values['counter'] = Counter
f.write(json.dumps(values))
f.close()




while True:
    #f.flush()
    # next create a socket object
    s = socket.socket()
    print("Socket successfully created")

    # reserve a port on your computer in our
    # case it is 12345 but it can be anything
    port = 12345

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', port))
    print("socket binded to %s" % (port))

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    message = input('Enter a message:')

    #binary_hash = Hash(message, hash_key)

    ciphers = []
    start_time=time.time()
    if mode_of_operation == '2':
        ciphers = CBC(message, key, IV)
    elif mode_of_operation == '1':
        ciphers = ECB(message, key)
    elif mode_of_operation == '3':
        ciphers = CFB(message, key, IV)
    elif mode_of_operation == '4':
        ciphers = CTR(message, key, Counter)
    end_time = time.time()
    print('Time taken',end_time-start_time)
    hash=hmac(ciphers,hash_key)
    ciphers.append(hash)

    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # send a thank you message to the client.
    print("Messages After Encryption: ",ciphers)
    c.send(bytearray(str(ciphers).encode()))
    # Close the connection with the client
    c.close()