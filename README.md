# CYSE130ProjectREADME

This project aims to design and overall plan out a cybersecurity system for a theoretical company. 
Throughout this project, we have utilized system engineering principles, UML modeling, and Python
automation in order to create this comprehensive cybersecurity system. 

To view the UML models, simply go to the "Group Project CYSE130" folder and then go to the 
"Group Project Initial Planning and Design Week-5" folder. From there, the "System Requirements Document" 
file provides a SysML System Requirement diagram link provided in a powerpoint, and a UML diagram link that
provides a UML diagram. There is also a list of the requirements categorized by number, with each subsection
underneath each specific requirement. 

To view the Automation assignment, go to the "Group Project CYSE130" folder and then go to the
"Group Project Automation Assignment" folder. From there, there are 4 separate Python files that each represent
a task based on the challenge needed to solve. There is also an Automation Report file that provides the description
of each task and the intended goal. 

In order to run "CYSE130-Task1.py" task, take the code and paste it into a Python interpreter, such as VSC. Download the 
"Linux_2k.log" file. Then, in order to run it, make sure to replace the "path" variable with a path to the Linux_2k.log 
file on your system, as it may vary depending on the structure of your system's files. Then, run the code and once it finishes,
a file called "summary_logs.txt" that provides a summary of how manylogin anomalies are provided based on the Linux security log. 

In order to run "CYSE130-Task2.py", take the code and paste it into a Python interpreter. Then, just simply run the code. Depending
on what you set the interval to (default value is currently set to 5 seconds), you will receive an update about your cpu and memory
usage as a percent, and it will be outputted to a file called "performance_data.txt", and then if the percentage is higher than a specific
threshold, current value is set to >85, then it will print an alert saying its too high and output that message to another file called,
"performance_alert.txt". 

In order to run "Task3.py", take the code and paste it into a Python interpreter. Then, in order to run it, make sure you change the msg['From']
email and the msg['To'] email to make sure that it sends to your email. Also, make sure to change the parameters in the "smtp.login()" method to 
match your email. Then, it will automatically run and send you an email if your cpu or memory percentage exceeds a certain threshold, outlined in 
Task2. 

In order to run "automation part 4 (vulnerability scan)", take the code and paste it into VSC, and then run the first code segment, which installs
the python nmap. Then run the second code segment, which imports it. Then, all you have to do is change the "target" variable to whatever your target
IP address or hostname is. Also, if you want to scan a different set of ports, then in the "nm.scan()" method, change the second parameter to fit whatever
ports you want to check. Then, the output will be printed. 
