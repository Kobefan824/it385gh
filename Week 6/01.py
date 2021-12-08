#!/user/bin/en python3

import paramiko
import time
from getpass import getpass

# Get remote node's login info
node_u = 'justincase' #input("enter username:")
node_p = getpass("Enter password: ")
db1_ip = '192.168.0.121'
web1_ip = '192.168.0.111'

cmd = 'hostname; ls -lrt; ifconfig'
conn = paramiko.SSHClient()

conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

conn.connect(web1_ip, username = node_u, password = node_p)
mystdin, mystdout, mystderr = conn.exec_command(command=cmd)

output = mystdout.readlines()
for eachline in output:
    print(eachline.strip())

error = mystdout.read().decode().strip()
print (error)

conn.close()
