'''
This code segment is a function that takes in the subject and the body of the email that the user wishes
to send, and it creates an email with a specific starting email address and a destination email address, 
in this case a group member's two emails, and then it logs in to the starting email and sends the message.
This function is a partner function with Task 2, as the performance_monitoring function calls on the send_alert 
function whenever an alert (in this case CPU and memory > 85) is needed. 
'''

import psutil
import smtplib 
from email.message import EmailMessage 

def performance_monitoring():
    while(True):
        current_cpu_usage = psutil.cpu_percent(interval=5)
        print(f"Current CPU Usage: {current_cpu_usage}%")

        current_memory_info = psutil.virtual_memory()
        print(f"Memory usage: {current_memory_info.percent}%\n")

        with open("performance_data.txt", "a") as file:
            file.write(f"Current CPU: {current_cpu_usage}%, Current Memory: {current_memory_info.percent}%\n")

        if(current_cpu_usage > 85):
            send_alert('High CPU Usage Alert', f'CPU usage is currently at {current_cpu_usage}%')
            print(f"ALERT: High CPU usage detected, with the CPU value being {current_cpu_usage}%\n")
            with open("performance_alert.txt", "a") as f:
                f.write(f"ALERT: {current_cpu_usage}% CPU Usage is too high\n")

        if(current_memory_info.percent > 85):
            send_alert('High Memory Usage Alert', f'Memory usage is currently at {current_memory_info.percent}%')
            print(f"ALERT: High memory usage detected, with the memory being {current_memory_info.percent}%\n")
            with open("performance_alert.txt", "a") as f2:
                f2.write(f"ALERT: {current_memory_info.percent}% Memory Usage is too high\n")

def send_alert(subject, body):
    msg = EmailMessage() 
    msg.set_content(body) 
    msg['Subject'] = subject 
    msg['From'] = 'xarias356@gmail.com' 
    msg['To'] = 'ariasariel2006@gmail.com' 

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
        smtp.login('xarias356@gmail.com', 'llka legy mlhn gfrk') 
        smtp.send_message(msg) 

performance_monitoring()
