# SUR: Sanctuarizing Unaccompanied Refugees Data

**SUR** (Sanctuarizing Unaccompanied Refugees) is a proof-of-concept cryptographic infrastructure designed to protect the data of unaccompanied minors in humanitarian settings. It extends the Q2CSI framework to encode data relationally using three security layers: Iron, Gold, and Clay.

## Features
- Canonical context-aware hashing of child protection records
- Kinship vector hashing based on Ubuntu ethics
- Layered encoding model based on the CRO trilemma (Confidentiality, Reliability, Opposability)

## Structure
### data
- Chikdren Dataset (a JSON file)
### doc
- Mariam's Case: A case study examining the application of the SUR infrastructure through the journey of Mariam, a 10-year-old Mafa girl from Cameroon
- SUR Core Crypto: The complete cryptographic specification of the SUR infrastructureLayered encoding model based on the CRO trilemma (Confidentiality, Reliability, Opposability)
- The SUR Project: The overview of the SUR infrastructure, a Secure, Universal, and Responsible cryptographic framework rooted in African ethical paradigms
#### figures
- empty up to now.
### examples
- Mariam demo: The demonstration of the working process of SUR on the Mariam's case
- SUR Core Crypto: The complete cryptographic specification of the SUR infrastructure Layered encoding model based on the CRO trilemma (Confidentiality, Reliability, Opposability)
- test output: The output from the processing of Mariam's case
### letter
- AfroLeadership Institutional Endorsement Letter for the Kluz Prize for PeaceTech
- The Covert Letter for the SUR Project Submission
### src
- Encoder: The script illustrating a minimal context-aware hashing prototype for SUR PoC
- Kinship hash:The Implementation of the Ubuntu-informed canonical hashing for relational vectors
- Mariam's PoC: This script illustrates a minimal context-aware hashing prototype for Mariam's case
- utils: A minimal python script for .JSON file 
### requirements: the minimal runtime environment for the SUR execution

## Getting Started

### Prerequisites
- Python 3.8+
- Run: `pip install -r requirements.txt`

### Demo
```bash
cd examples
bash mariam_demo.sh
```

## References
- [Q2CSI ePrint 2025/1380](https://eprint.iacr.org/2025/1380)
- [CRO Trilemma ePrint 2025/1348](https://eprint.iacr.org/2025/1348)
- See `/doc/` for technical documentation and diagrams

## Contacts
#### Afroleadership
- contact@afroleadership.org
#### The SUR Project
- sur@afroleadership.org
#### The Founder and President, AfroLeadership 
- charlie@afroleadership.org
#### The Research Director
- thierry@afroleadership.org
- minkathierry@gmail.com

## The Team Leader
Thierry Emmanuel MINKA MI NGUIDJOI
Ph.D. Candidate in Theoretical Cryptography
(LIMSI, ENSP, University of Yaoundé I)
Judicial Expert in Cybersecurity
