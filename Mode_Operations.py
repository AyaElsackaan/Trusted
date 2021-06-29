import binascii
from Des import Des_Encrypt
def Ascii_to_binary(str,n):
    a_byte_array = bytearray(str, "ascii")
    byte_list = []
    result=[]

    for byte in a_byte_array:
        binary_representation = bin(byte)[2:]
        byte_list.append(binary_representation)
        while len(byte_list[-1]) < 8:
            byte_list[-1] = '0' + byte_list[-1]
    #print(byte_list)
    for i in range(0,len(byte_list),n):
        result.append(''.join(byte_list[i:i+n]))
    #result.append(hash[0:64])
    #result.append(hash[64:])
    #for i in range(0,len(hash),n*8):
    #    result.append(''.join(hash[i:i+n*8]))
    #print(result)
    return result

def ECB(message,key):
    blocks=Ascii_to_binary(message,8)
    ciphers=[]
    for block in blocks:
        ciphers.append(Des_Encrypt(key,block,True))
    return ciphers
def ECB_Decrypt(ciphers,key):
    blocks=[]
    for cipher in ciphers:
        blocks.append(Des_Encrypt(key,cipher,False))
    return blocks
def CBC(message,key,IV):
    pre_cipher=[IV]
    ciphers=[]
    blocks = Ascii_to_binary(message,8)
    for i in range(len(blocks)):
        outputofxor = bin(int(blocks[i], 2) ^ int(pre_cipher[i], 2))[2:]
        xorlist = list(outputofxor)
        while len(xorlist) < 64:
            xorlist.insert(0, '0')
        outputofxor = ''.join(xorlist)
        ciphers.append(Des_Encrypt(key,outputofxor,True))
        pre_cipher.append(ciphers[-1])
    return ciphers

def CBC_Decrypt(ciphers,key,IV):
    pre_cipher=[IV]+ciphers
    blocks=[]
    for i in range(len(ciphers)):
        curr_plain_text=Des_Encrypt(key,ciphers[i],False)
        outputofxor = bin(int(curr_plain_text, 2) ^ int(pre_cipher[i], 2))[2:]
        xorlist = list(outputofxor)
        while len(xorlist) < 64:
            xorlist.insert(0, '0')
        outputofxor = ''.join(xorlist)
        blocks.append(outputofxor)
    return blocks
def CFB(message,key,IV):
    pre_cipher=[IV]
    ciphers=[]
    blocks = Ascii_to_binary(message,1)
    for i in range(len(blocks)):
        encrypted_output=Des_Encrypt(key, pre_cipher[i], True)
        select_s_left=encrypted_output[0:8]
        outputofxor = bin(int(blocks[i], 2) ^ int(select_s_left, 2))[2:]
        xorlist = list(outputofxor)
        while len(xorlist) < 8:
            xorlist.insert(0, '0')
        outputofxor = ''.join(xorlist)
        pre_cipher.append(pre_cipher[-1][8:64]+outputofxor)
        ciphers.append(outputofxor)
    return ciphers
def CFB_Decrypt(ciphers,key,IV):
    pre_cipher=[IV]
    blocks=[]
    for i in range(len(ciphers)):
        encrypted_output=Des_Encrypt(key, pre_cipher[i], True)
        select_s_left=encrypted_output[0:8]
        outputofxor = bin(int(ciphers[i], 2) ^ int(select_s_left, 2))[2:]
        xorlist = list(outputofxor)
        while len(xorlist) < 8:
            xorlist.insert(0, '0')
        outputofxor = ''.join(xorlist)
        pre_cipher.append(pre_cipher[-1][8:64]+ciphers[i])
        blocks.append(outputofxor)
    return blocks
def CTR(message,key,counter):
    blocks=Ascii_to_binary(message,8)
    ciphers=[]
    for block in blocks:
        temp=Des_Encrypt(key, counter, True)
        counter=bin(int(counter,2)+1)[2:]
        counterlist = list(counter)
        while len(counterlist) < 64:
            counterlist.insert(0, '0')
        counter = ''.join(counterlist)
        outputofxor = bin(int(counter, 2) ^ int(block, 2))[2:]
        xorlist = list(outputofxor)
        while len(xorlist) < 8:
            xorlist.insert(0, '0')
        outputofxor = ''.join(xorlist)
        ciphers.append(outputofxor)
    return ciphers
def CTR_Decrypt(ciphers,key,counter):
    blocks=[]
    for cipher in ciphers:
        temp=Des_Encrypt(key, counter, True)
        counter=bin(int(counter,2)+1)[2:]
        counterlist = list(counter)
        while len(counterlist) < 64:
            counterlist.insert(0, '0')
        counter = ''.join(counterlist)
        outputofxor = bin(int(counter, 2) ^ int(cipher, 2))[2:]
        xorlist = list(outputofxor)
        while len(xorlist) < 8:
            xorlist.insert(0, '0')
        outputofxor = ''.join(xorlist)
        blocks.append(outputofxor)
    return blocks
def binary_to_ascii(bin_blocks):
    result_str=""
    for bin_block in bin_blocks:
        n = int(bin_block, 2)
        result_str=result_str+binascii.unhexlify('%x' % n).__str__()[2:-1]
    return result_str
#ciphers=CTR('Hellloooooo I I am Aya','1101111011001001000001110101001110100101110110001100111111011111','1101111011010010000011101010011101001011101100011001111110111111')
#blocks=CTR_Decrypt(ciphers,'1101111011001001000001110101001110100101110110001100111111011111','1101111011010010000011101010011101001011101100011001111110111111')
#print("blocks",blocks)
#msg=binary_to_ascii(blocks)
#print(msg)





