from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def aes_decrypt(data, key):
    raw_data = base64.b64decode(data)
    iv = raw_data[:AES.block_size]
    ct = raw_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')

#aaa
#bbb
