import json
from collections import defaultdict 
from collections import Counter

def get_counts(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

def top_counts(count_dict, n=5):
    value_key_pairs = [(count, name) for name, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

def top_issues_by_project(issues, n=3):
    value_key_pairs = [(count,name) for name, count in issues.items()]
    return value_key_pairs[-n:] 

def open_issues(count_dict):
    items = [{ 'id': item['id'], 'name': item['project']['name'], 'subject': item['subject']} 
            for item in count_dict if 'status' in item and item['status']['name'] == 'Nueva']
    return items
        
path = "/home/ruben/Development/datapy/issues.json"
issues = [json.loads(line) for line in open(path)]
records = issues[0]['issues']
ninjas = [rec['assigned_to']['name'] for rec in records if 'assigned_to' in rec]
status = [rec['status']['name'] for rec in records if 'status' in rec]
#counts = get_counts(ninjas)
counts = Counter(ninjas)
o_issues = open_issues(records)