import json

def load_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)['children']

def canonical_string(entry):
    fields = [
        entry['id'], entry['name'], str(entry['age']), entry['gender'],
        entry['nationality'], entry['status'], entry['guardian'],
        entry['authorized_action'], entry['valid_from'], entry['valid_until'],
        "|".join(sorted(entry['legal_basis']))
    ]
    return "||".join(fields)
