import json

# Opening JSON file
f = open('string.json',)

# returns JSON object as
# a dictionary
data = json.loads(f)

# Iterating through the json
# list
for each in data['totals']:
    print(each['msg_time_mean_avg'])

# Closing file
f.close()
