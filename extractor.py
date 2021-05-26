import psutil
import csv
import sys

experiment_number = sys.argv[1]
iteration_times = int(sys.argv[2])

fields = ["cpu_usage_percent",
          "cpu_freq_current",
          "memory_total",
          "memory_available",
          "memory_percent",
          "memory_used",
          "memory_free",
          "swap_used",
          "swap_percent",
          "cpu_temperature"]

with open('run_'+str(experiment_number)+'.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)

    i = 0
    while i < iteration_times:

        cpu_usage_percent = psutil.cpu_percent(interval=1, percpu=False)
        cpu_freq_current = psutil.cpu_freq().current
        memory_total =  psutil.virtual_memory().total
        memory_available = psutil.virtual_memory().available
        memory_percent = psutil.virtual_memory().percent
        memory_used = psutil.virtual_memory().used
        memory_free = psutil.virtual_memory().free
        swap_used = psutil.swap_memory().used
        swap_percent = psutil.swap_memory().percent

        cpu_temperature = psutil.sensors_temperatures()
        for entry in cpu_temperature['cpu_thermal']:
            cpu_temperature = psutil.sensors_temperatures()


        rows = [[cpu_usage_percent, cpu_freq_current, memory_total, memory_available,
                 memory_percent, memory_used, memory_free, swap_used, swap_percent, cpu_temperature]]

        write.writerows(rows)
        i = i + 1

