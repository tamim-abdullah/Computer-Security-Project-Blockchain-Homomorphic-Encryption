from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def run_rsa(data):
    # Generate key pair (for demo/benchmark only)
    key = RSA.generate(2048)
    public_key = key.publickey()
    
    # Encrypt using public key
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(data.encode())
    
    # Optional: Decrypt (if you want to demonstrate full flow)
    # decrypt_cipher = PKCS1_OAEP.new(key)
    # decrypted = decrypt_cipher.decrypt(encrypted)

    # return decrypted.decode()  # For checking
    return encrypted
