#!/usr/bin/env python3

import paramiko
import time
from getpass import getpass


n_username = 'justincase' 
n_password = 'Password01' 
web1_ip = '192.168.0.111'
db1_ip = '192.168.0.121'


command = 'sudo -S groupadd wheel; sudo -S useradd "stranger" -c "Stranger Danger" -G "wheel" -m -p "Password01"; ping -c 4 db1'

conn = paramiko.SSHClient()

conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

conn.connect(web1_ip, username=n_username, 
            password=n_password)



mystdin, mystdout, mystderr = conn.exec_command(command)

mystdin.write('Password01\n')
mystdin.flush()

output = mystdout.readlines()
for line in output:
    print(line.strip())


error = mystderr.read().decode().strip()
print(error)

conn.close()

del conn, mystdin, mystdout, mystderr, output, error