'''
This code segment is a function that takes in the path of the security log, which in this case I chose
a linux security log, and then it goes through the file and looks for where the file has the phrase
"authentication failure" and then adds that into the anomaly log that was created. Then it creates
a report as a file called summary_logs.txt, that first says the total amount of suspicious activity,
then writes each log within the anomaly log into the summary_logs.txt file. 
'''
def analyze_logs(path):
    with open(path, 'r') as f:
        logs = f.readlines()
    login_anomaly_log = [log for log in logs if 'authentication failure' in log.lower()]

    with open('summary_logs.txt', 'w') as sum_file:
        sum_file.write(f"Total suspicious logs found: {len(login_anomaly_log)}\n")
        for log in login_anomaly_log:
            sum_file.write(log + '\n')


path = r"C:\Users\rasha\Downloads\Linux_2k.log"
analyze_logs(path)