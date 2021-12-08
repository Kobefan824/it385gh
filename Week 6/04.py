#!/usr/bin/env python3

import paramiko
from getpass import getpass

csr_ip = '192.168.0.11'
n_username  = 'cisco'
n_password = 'cisco'

cmd = 'show ip int brief'
conn = paramiko.SSHClient()

conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect(csr_ip, username = n_username, password = n_password)
mystdin, mystdout, mystderr = conn.exec_command(cmd)

output = mystdout.readlines()

for line in output:
    print(line.strip())

conn.close
del conn, mystdin, mystdout, mystderr