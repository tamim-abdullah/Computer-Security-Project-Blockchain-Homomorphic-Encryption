from phe import paillier

def run_paillier(data):
    pub, priv = paillier.generate_paillier_keypair()
    pub.encrypt(len(data))  # Sample encryption of size
