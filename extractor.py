import csv
import sys
import datetime as dt
import psutil

experiment_number = sys.argv[1]

fields = ["time",
          "cpu_usage_percent",
          "cpu_freq_current",
          "memory_total",
          "memory_available",
          "memory_percent",
          "memory_used",
          "memory_free",
          "swap_used",
          "swap_percent",
          "packets_received",
          "cpu_temperature"]

with open('run_'+str(experiment_number)+'.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)

    while True:

        cpu_usage_percent = psutil.cpu_percent(interval=1, percpu=False)
        cpu_freq_current = psutil.cpu_freq().current
        memory_total =  psutil.virtual_memory().total
        memory_available = psutil.virtual_memory().available
        memory_percent = psutil.virtual_memory().percent
        memory_used = psutil.virtual_memory().used
        memory_free = psutil.virtual_memory().free
        swap_used = psutil.swap_memory().used
        swap_percent = psutil.swap_memory().percent
        network_pkt_recv = psutil.net_io_counters(pernic=True)
        network_pkt_recv = network_pkt_recv['eth0'][3]
        cpu_temperature = psutil.sensors_temperatures()
        for entry in cpu_temperature['cpu_thermal']:
            cpu_temperature = entry.current



        rows = [[dt.datetime.now().time(),cpu_usage_percent, 
                 cpu_freq_current, memory_total, memory_available,
                 memory_percent, memory_used, memory_free, swap_used, 
                 swap_percent, network_pkt_recv,cpu_temperature]]

        write.writerows(rows)


