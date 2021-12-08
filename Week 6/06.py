#!/ust/bin/env python3

import paramiko
from getpass import getpass
import time

csr_ip = '192.168.0.11'
user = 'cisco'
passwd = 'cicso'

conn = paramiko.SSHClient()

conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect(csr_ip, username=user, password=passwd)

session = conn.invoke_shell()
session.send('terminal length 0\n')

session.send('sho ip int brief\n')
time.sleep(3)
output = session.recv(10000).decode()
time.sleep(1)

print("\n\n")
session.send('conf t\n')

time.sleep(0.5)
output = session.recv(5000).decode()
print(output)

print(str(output)+ '\n')
time.sleep(0.5)
session.send('end\n')

stdoutList = []
for line in output:
    stdoutList.append(line.strip())

for item in stdoutList:
    primt(item)

conn.close()