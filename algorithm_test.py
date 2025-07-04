import time
from homomorphic.paillier_encrypt import run_paillier
from algorithms.aes_encrypt import run_aes
from algorithms.rsa_encrypt import run_rsa
from algorithms.ecc_encrypt import run_ecc

patient_data = "Name: Sara, Age: 30, Condition: Asthma"

def benchmark(name, func):
    start = time.time()
    func(patient_data)
    end = time.time()
    return round(end - start, 6)

results = {
    "Paillier": benchmark("Paillier", run_paillier),
    "AES": benchmark("AES", run_aes),
    "RSA": benchmark("RSA", run_rsa),
    "ECC": benchmark("ECC", run_ecc),
}

for name, t in results.items():
    print(f"{name} → {t} sec")
