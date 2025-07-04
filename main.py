from phe import paillier
from web3 import Web3
import hashlib
import json

# 1. Homomorphic Encryption
public_key, private_key = paillier.generate_paillier_keypair()

age = 30
diagnosis = 2  # Example numeric diagnosis code

encrypted_age = public_key.encrypt(age)
encrypted_diagnosis = public_key.encrypt(diagnosis)

print(f"Encrypted Age: {encrypted_age}")
print(f"Encrypted Diagnosis: {encrypted_diagnosis}")

# 2. Hash encrypted data (you only store hash on-chain, not encrypted values directly)
data_to_hash = str(encrypted_age.ciphertext()) + str(encrypted_diagnosis.ciphertext())
hash_hex = hashlib.sha256(data_to_hash.encode()).hexdigest()

print("Hash to send to blockchain:", hash_hex)

# 3. Connect to Ganache
ganache_url = "http://127.0.0.1:7545"  # Check this is correct
w3 = Web3(Web3.HTTPProvider(ganache_url))

if w3.is_connected():
    print("Connected to Ethereum network ✅")
else:
    print("❌ Failed to connect to Ethereum network")
    exit()

# 4. Use your ABI here
abi = [
    {
        "inputs": [
            {"internalType": "address", "name": "", "type": "address"}
        ],
        "name": "ehrDataHashes",
        "outputs": [
            {"internalType": "string", "name": "", "type": "string"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# 5. Deployed contract address from Truffle
contract_address = "0x48b3E8c64e681DcbB85006810744FB33a3313382"

contract = w3.eth.contract(address=contract_address, abi=abi)

# 6. Sending the hash requires a function to write it to blockchain.
# If your smart contract only has a `view` function, add a `storeHash(string hash)` function in Solidity.
# For now, trying to call view-only will fail to write

# Example: calling a read function (but writing won't work unless smart contract has write function)
# account = w3.eth.accounts[0]
# contract.functions.storeHash(hash_hex).transact({'from': account})

# ❗ If your contract doesn’t have `storeHash` yet, we need to update Solidity to include:
'''
function storeHash(string memory hash) public {
    ehrDataHashes[msg.sender] = hash;
}
'''

