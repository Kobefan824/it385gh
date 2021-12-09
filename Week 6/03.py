
import paramiko
import time

n_username = 'justincase' 
n_password = 'Password01' 
hostnode = '192.168.0.111'

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostnode, 
        username = n_username,
        password=n_password)
    
    
    while True:
        try:
            
            command = input("$> ")
            
            
            if command == "exit": break    

            
            mstdin, mstdout, mstderr = client.exec_command(command)            
            
            
            print(mstdout.read().decode())
            
            
            print(mstderr.read().decode())
        except KeyboardInterrupt:
            
            break
   
except Exception as err:
    print(str(err))

finally:
    client.close()