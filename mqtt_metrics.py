import json
import os

# Opening JSON file

stream = os.popen('/home/ubuntu/go/bin/mqtt-benchmark --broker tcp://10.0.0.4:1883 --count 100 --size 100 --clients 100 --qos 2 --format json --quiet')
output = stream.readlines()

print(output)
data = json.load(output)
print(data['totals']['msg_time_mean_avg']) 
