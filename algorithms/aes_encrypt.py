from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def run_aes(data):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    
    # Optional: Decrypt to verify
    decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
    pt = unpad(decipher.decrypt(ct_bytes), AES.block_size)
    return pt.decode()
