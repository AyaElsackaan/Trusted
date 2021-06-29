# Import socket module
import socket
import ast
import json
from Mode_Operations import *
from Hashing import*
#import hashlib



f=open('config.txt', 'r')
values = json.load(f)
f.close()
while True:
    # Create a socket object
    s = socket.socket()

    # Define the port on which you want to connect
    import os

    port = 12345

    # connect to the server on local computer
    s.connect(('127.0.0.1', port))
    # receive data from the server
    lst = s.recv(1024).__str__()[2:-1]
    ciphers = ast.literal_eval(lst)
    print("received message before decryption",ciphers)
    calculated_hash=ciphers[-1]
    print('calculated hash:',calculated_hash)
    ciphers=ciphers[:-1]
    hash=hmac(ciphers,values['hash_key'])
    print('recived hash:', hash)
    if calculated_hash==hash:
        print('Valid mac')
    else:
        print('Invalid mac')
        continue
    blocks=[]
    if values['mode']=='1':
        blocks=ECB_Decrypt(ciphers,values['key'])
    elif values['mode'] == '2':
        blocks = CBC_Decrypt(ciphers, values['key'],values['IV'])
    elif values['mode'] == '3':
        blocks = CFB_Decrypt(ciphers, values['key'],values['IV'])
    elif values['mode'] == '4':
        blocks = CTR_Decrypt(ciphers, values['key'],values['counter'])

    plain_text=binary_to_ascii(blocks)
    print("The plain text is:",plain_text)




    # close the connection
    s.close()