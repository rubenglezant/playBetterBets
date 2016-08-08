import paramiko

paramiko.util.log_to_file('ssh.log') # sets up logging

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('192.168.1.137', username='pi', password='raspberry')
stdin, stdout, stderr = ssh.exec_command("df -h")
stdin.write('lol\n')
stdin.flush()

data = stdout.read().split('\n')
print (data)
for line in data:
    print line
