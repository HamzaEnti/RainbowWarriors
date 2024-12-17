from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

def aes_encrypt(data, master_key):
    cipher = AES.new(master_key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return base64.b64encode(cipher.iv + ct_bytes).decode('utf-8')

def aes_decrypt(data, master_key):
    raw_data = base64.b64decode(data)
    iv = raw_data[:AES.block_size]
    ct = raw_data[AES.block_size:]
    cipher = AES.new(master_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')

