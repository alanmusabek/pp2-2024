import json
with open('./sample-data.json', 'r') as sampleData_file:
    sampleData = json.load(sampleData_file)
    print(sampleData)