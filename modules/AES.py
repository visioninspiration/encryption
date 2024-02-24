from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64

def encryption(text, password):
    text = text.encode("utf8")
    pw = password.encode("utf8")
    key = hashlib.pbkdf2_hmac(hash_name='sha256', password=pw, salt=b'#*a1!+^A', iterations=100000)
    aes = AES.new(key, AES.MODE_ECB)
    bsize = 256
    padded = pad(text, bsize)
    encrypted_text = aes.encrypt(padded)
    print(f"Encrypted text (bytes): {encrypted_text}")
    print("")
    encoded = str(base64.b64encode(encrypted_text), "utf-8")
    print(f"Encrypted text (base64): {encoded}")
    return encoded

def decryption(encrypted_text, password):
    encrypted_text = base64.b64decode(encrypted_text)
    pw = password.encode("utf8")
    key = hashlib.pbkdf2_hmac(hash_name='sha256', password=pw, salt=b'#*a1!+^A', iterations=100000)
    aes = AES.new(key, AES.MODE_ECB)
    decrypted_text = aes.decrypt(encrypted_text)
    bsize = 256
    original = unpad(decrypted_text, bsize)
    original = original.decode("utf8")
    return original
