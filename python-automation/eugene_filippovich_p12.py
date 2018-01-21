import paramiko
import logging

logging.basicConfig(level=logging.INFO)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
file = open('E:\Config_file.txt', 'r')
for line in file:
    info = {}
    info['ip'] = line.split(' ')[0]
    info['hostname'] = line.split(' ')[1]
    info['username'] = line.split(' ')[2]
    info['password'] = line.split(' ')[3]

    def connecting():
        ssh.connect(info['ip'], username=info['username'], password=info['password'])
        logging.info(' Files viewed from {} ({}) machine'.format(info['hostname'], info['ip']))
    try:
        connecting()

    except Exception:
        logging.warning(" Connection Failed. Check your config file")
        quit()


    stdin, stdout, stderr = ssh.exec_command("ls /etc/")

    for line in stdout.readlines():
        print line.strip()
    ssh.close()
