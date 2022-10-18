import binascii
import string
import random
 
def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)
 
def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def encrypt(msg,key):
    msg = bytes(msg, encoding = 'ascii')
    key = bytes(key, encoding = 'ascii')
    key = toHex(key)
    msg = toHex(msg)
    code = msg^key
    return code
print(encrypt("hei","abc"))

def decrypt(code,key):
    key = bytes(key, encoding = 'ascii')
    key = toHex(key)
    msg= code^key
    msg = toString(msg)
    return msg
print(decrypt(encrypt("hei","abc"),"abc"))

def main():
    msg = input("hva er meldingen?")
    key=[]
    for i in range(len(msg)):
        key.append(string.ascii_lowercase[random.randint(0,len(msg))])
    print(key)
    key="".join(key)
    print(key)
    code = encrypt(msg,key)
    print("kryptert",code)
    print("meldingen din",decrypt(code,key))
main()