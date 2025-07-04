from phe import paillier

# Generate keypair once (in real apps, you would store/reuse these)
public_key, private_key = paillier.generate_paillier_keypair()

def encrypt_value(value):
    return public_key.encrypt(value)

def decrypt_value(encrypted_value):
    return private_key.decrypt(encrypted_value)

def get_keys():
    return public_key, private_key
