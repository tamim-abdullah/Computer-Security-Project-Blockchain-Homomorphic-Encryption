# Title: Blockchain Based Medical Report Encryption

**Course:** CSE 4531 Computer Security  
**Group Members:**  
- Tamim Abdullah (011211072)  
- MD Redwan Rahman Ornob (011211001)  
- Mahmud Hasan Shanto (011213052)  
- Nousin Rahman Nahin (0112310573)  

---

## Motivation of this project

Medical reports are crucial for proper treatment, but they can be altered with bad intentions, leading to misdiagnosis, incorrect treatments, and legal complications. To ensure trust between patients, doctors, and hospitals, we need a secure system that prevents unauthorized changes.

We propose to use blockchain-based technology to protect medical records. Any modification is permanently recorded, showing unauthorized changes to the reports, ensuring transparency and easy tracking of report updates. Our goal is to use homomorphic encryption and blockchain technology to develop a security framework preventing fraudulent activities related to medical records.

---

## Plan of Execution

1. Utilize a distributed ledger to store encrypted medical records, ensuring data integrity and availability.
2. Implement homomorphic encryption to allow computations on encrypted data without revealing sensitive information. Before uploading to the blockchain, encrypt medical records using homomorphic encryption techniques.
3. Store the encrypted data on the blockchain, ensuring traceability.
4. Implement smart contracts to manage data access permissions, data sharing, and consent management, ensuring only authorized entities can access specific records.
5. Maintain logs of data access and modifications to enhance transparency and accountability.

---

## Benefits

| **Benefit**                  | **Description**                                                                 |
|------------------------------|------------------------------------------------------------------------------|
| Medical records stay untouched | Blockchain ensures no one can modify or tamper with stored medical reports (Test results, Prescriptions, etc.) |
| Patient data remains private   | Homomorphic encryption ensures sensitive pieces of information remain protected |
| Secure data processing         | Homomorphic encryption allows queries and computations without decrypting patient data |
| Every action is traceable      | A verifiable audit trail logs every access and modification |
| Only the right people get access | Smart contracts strictly control who can view or modify records |
| Full transparency              | Keeping logs of all access ensures accountability and trust |

---
