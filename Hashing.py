import hashlib
def Hash(message,key):
    x=message+key
    result_hash = hashlib.md5(x.encode())
    binary_hash=bin(int(result_hash.hexdigest(),16))[2:]
    hashlist = list(binary_hash)
    while len(hashlist) < 128:
        hashlist.insert(0, '0')
    binary_hash = ''.join(hashlist)
    return binary_hash
def hmac(blocks,key):
    ipad='00110110'*21
    keylist=list(key)
    message=''.join(blocks)
    while len(keylist) < 168:
        keylist.insert(0, '0')
    outputofxor = bin(int(ipad, 2) ^ int(key, 2))[2:]
    xorlist = list(outputofxor)
    while len(xorlist) < 168:
        xorlist.insert(0, '0')
    outputofxor = ''.join(xorlist)
    message=outputofxor+message
    hash=bin(int(hashlib.sha1(message.encode()).hexdigest(), 16))[2:]
    hashlist = list(hash)
    while len(hashlist) < 168:
        hashlist.insert(0, '0')
    hash = ''.join(hashlist)
    opad='01011100'*21
    outputofxor = bin(int(opad, 2) ^ int(key, 2))[2:]
    xorlist = list(outputofxor)
    while len(xorlist) < 168:
        xorlist.insert(0, '0')
    outputofxor = ''.join(xorlist)
    hash=outputofxor+hash
    hash = bin(int(hashlib.sha1(hash.encode()).hexdigest(), 16))[2:]
    hashlist = list(hash)
    while len(hashlist) < 160:
        hashlist.insert(0, '0')
    hash = ''.join(hashlist)
    return hash
#message='101010101010101010'
#print(bin(int(hashlib.sha1(message.encode()).hexdigest(),16))[2:])


