'''
This code segment is a function that looks at the current cpu and memory usage with an interval of
5 seconds and then outputs what the percentage is for both of them, then it opens a file called
performance_data.txt and then puts that information onto there as well. Then, the metrics being used
here for problems or alerts is if either the cpu usage or memory usage is greater than 85%, in which
it outputs an alert saying that the percentage is too high. It also opens a file called performance_alert.txt
in which it puts that information onto there as well. Since this is a program to monitor performance, 
there is an infinite loop since the performance should be checked constantly, and would need manual
interruption to end the program. 
'''

import psutil

def performance_monitoring():
    while(True):
        current_cpu_usage = psutil.cpu_percent(interval=5)
        print(f"Current CPU Usage: {current_cpu_usage}%")

        current_memory_info = psutil.virtual_memory()
        print(f"Memory usage: {current_memory_info.percent}%\n")

        with open("performance_data.txt", "a") as file:
            file.write(f"Current CPU: {current_cpu_usage}%, Current Memory: {current_memory_info.percent}%\n")

        if(current_cpu_usage > 85):
            print(f"ALERT: High CPU usage detected, with the CPU value being {current_cpu_usage}%\n")
            with open("performance_alert.txt", "a") as f:
                f.write(f"ALERT: {current_cpu_usage}% CPU Usage is too high\n")

        if(current_memory_info.percent > 85):
            print(f"ALERT: High memory usage detected, with the memory being {current_memory_info.percent}%\n")
            with open("performance_alert.txt", "a") as f2:
                f2.write(f"ALERT: {current_memory_info.percent}% Memory Usage is too high\n")

performance_monitoring()