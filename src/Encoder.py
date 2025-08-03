
# This script illustrates a minimal context-aware hashing prototype for SUR PoC
    
\begin{lstlisting}[
    language=Python,
    basicstyle=\scriptsize\ttfamily, % Taille réduite
    breaklines=true, % Césure des lignes
    postbreak=\mbox{\textcolor{red}{$\hookrightarrow$}\space},
    frame=single, % Encadrement
    framesep=2mm % Marge interne
]
Requirements: Python >= 3.8
# Updated to SHA3
import hashlib
digest = hashlib.sha3_256(canonical.encode('utf-8')).hexdigest()
import json
import hashlib
from datetime import datetime

# Utility Functions
def load_data(json_file): 
    with open(json_file, 'r', encoding='utf-8') as f: 
        return json.load(f)['children']

def canonical_string(entry): 
    """Produces canonical string representation of entry"""
    fields = [
        entry['id'],
        entry['name'],
        str(entry['age']),
        entry['gender'],
        entry['nationality'],
        entry['status'],
        entry['guardian'],
        entry['authorized_action'],
        entry['valid_from'],
        entry['valid_until'],
        "|".join(sorted(entry['legal_basis']))
    ]
    return "||".join(fields)

def hash_contextual_entry(entry): 
    """Hashes canonical string representation"""
    canonical = canonical_string(entry)
    digest = hashlib.sha3_256(canonical.encode('utf-8')).hexdigest()
    return digest

# Proof-of-Concept Execution (Mariam)
def main():
    data = load_data('children_data.json')
    target_id = 'CH-0001'  # Mariam's record
    mariam = next((child for child in data if child['id'] == target_id), None)
    
    if not mariam:
        print(f"Record {target_id} not found.")
        return
    
    print("=== Contextual Signature for Mariam ===")
    print("Canonical input:")
    print(canonical_string(mariam))
    print("\nContextual hash:")
    print(hash_contextual_entry(mariam))

if __name__ == '__main__': 
    main()
\end{lstlisting}

