import sys
import json
import os
import subprocess
import csv
import datetime as dt

# Opening JSON file


fields = ["time",
          "msg_time_mean_avg"]

messages_amount = sys.argv[1]
message_size = sys.argv[2]
client_amount = sys.argv[3]
qos_spec = sys.argv[4]
experiment_number = sys.argv[5]
experiment_times = sys.argv[6]
experiment_times = int(experiment_times)

with open('mqtt_messages_amount'+str(messages_amount)+'_message_size'+str(message_size)+'_client_amount'+str(client_amount)+'_qos_spec'+str(qos_spec)+'_experiment_numer'+str(experiment_number)+'_'+str(experiment_number)+'.csv', 'w') as f:

    write = csv.writer(f)
    write.writerow(fields)

    while experiment_times > 0:

        json_output = subprocess.check_output("/home/rodrigo/go/bin/mqtt-benchmark --broker tcp://192.168.0.2:1883 --count "+str(messages_amount)+" --size "+str(message_size)+" --clients "+str(client_amount)+" --qos "+str(qos_spec)+" --format json --quiet", shell=True).strip()

        json_output = json_output.decode()
        json_output = json.loads(json_output)

        #print(json_output['totals']['msg_time_mean_avg']) 
        msg_time_mean_avg= json_output['totals']['msg_time_mean_avg']


        rows = [[dt.datetime.now().time(),msg_time_mean_avg]]
        write.writerows(rows)

        #print(experiment_times)
        experiment_times = experiment_times - 1

    print("Finished!")
