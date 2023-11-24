import hashlib
from access import db

import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypts(password):
    password = hashlib.sha3_256(bytes(password, 'utf-8')).hexdigest()
    return password

def aesenc(password, user_id):
    """
    Encrypting passwords in records using aes-256 and hash of current user
    """
    password=bytes(password,'utf-8')
    hash = bytes(db.get_pass(user_id)[:32], 'utf-8')
    iv = get_random_bytes(16)
    encryptor = AES.new(hash, AES.MODE_CBC, iv)
    cipher_text = encryptor.encrypt(pad(password,16))
    #print(len(cipher_text))
    #print(len(iv))
    cipher_text = cipher_text.hex() + iv.hex()
    return cipher_text

def aesdec(password, user_id):
    """Decrypting passwrods"""
    #print(len(password))
    hash = bytes(db.get_pass(user_id)[:32], 'utf-8')
    cipher_text = bytes.fromhex(password[:32])
    iv = bytes.fromhex(password[32:])
    #print(len(iv))
    decryptor = AES.new(hash, AES.MODE_CBC, iv)
    password = unpad(decryptor.decrypt(cipher_text),16).decode('utf-8')
    return password




