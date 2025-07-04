from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

def run_ecc(data):
    # Generate ECC private key
    private_key = ec.generate_private_key(ec.SECP384R1())
    public_key = private_key.public_key()

    # Simulate encryption using a shared key derivation
    shared_key = private_key.exchange(ec.ECDH(), public_key)

    # Derive a key (like encrypting the shared key with hash)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data'
    ).derive(shared_key)

    # Just to simulate a real use case, we pretend we "used" it
    return derived_key
