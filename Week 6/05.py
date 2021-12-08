#pip3 install paramiko

import paramiko

hostname = '192.168.0.11'
port = 22
user = 'cisco'
passwd = 'cisco'

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=user, password=passwd)
    
    while True:
        try:
            cmd = input("$> ")
            if cmd == "exit": break
            stdin, stdout, stdeer = client.exec_command(cmd)
            print(stdout.read().decode())
        except KeyboardInterrupt:
            break

        client.close()

except Exception as err:
    print(str(err))