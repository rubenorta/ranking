import json
from collections import defaultdict 
def get_counts(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

def top_counts(count_dict, n=5):
    value_key_pairs = [(count, name) for name, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
        
path = "/home/ruben/Development/datapy/issues.json"
issues = [json.loads(line) for line in open(path)]
records = issues[0]['issues']
ninjas = [rec['assigned_to']['name'] for rec in records if 'assigned_to' in rec]
counts = get_counts(ninjas)

