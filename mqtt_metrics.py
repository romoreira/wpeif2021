import sys
import json
import os
import subprocess

# Opening JSON file


messages_amount = sys.argv[1]
message_size = sys.argv[2]
client_amount = sys.argv[3]
qos_spec = sys.argv[4]

json_output = subprocess.check_output("/home/ubuntu/go/bin/mqtt-benchmark --broker tcp://10.0.0.4:1883 --count "+str(messages_amount)+" --size "+str(message_size)+" --clients "+str(client_amount)+" --qos "+str(qos_spec)+" --format json --quiet", shell=True).strip()

json_output = json_output.decode()
json_output = json.loads(json_output)

print(json_output['totals']['msg_time_mean_avg']) 
