import json
from pandas import DataFrame

def get_by_status(count_dict,status):
    items = [{ 'id': item['id'], 'name': item['project']['name'], 'subject': item['subject']} 
            for item in count_dict if 'status' in item and item['status']['name'] == status]
    return items
    
def format_issue(issue):
    data = [issue['id'],issue['project']['name'],issue['status']['name'],issue['created_on'], issue['updated_on'], issue['subject']]
    if 'assigned_to' in issue:
        data.append(issue['assigned_to']['name'])
    else:
        data.append('')
    return data
    
path = "/home/ruben/Development/ranking/dump.json"
issues = [json.loads(line) for line in open(path)]
records = issues[0]

the_list = []
for record in records:
    the_list.append(format_issue(record))
    