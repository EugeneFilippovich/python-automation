import logging
import paramiko
import os

USERNAME = 'eugene'
logging.basicConfig(level=logging.INFO)


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
file = open('/home/eugene/Config_file', 'r')
ssh.connect('localhost', username='eugene', password='4356')
ssh.exec_command('mkdir -p ~/.ssh/')
ssh.exec_command('echo "%s" >> ~/.ssh/authorized_keys')
ssh.exec_command('chmod 600 ~/.ssh/authorized_keys')
ssh.exec_command('chmod 700 ~/.ssh/')
ssh.exec_command('ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -P ""')
ssh.close()

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

    ssh.exec_command('mkdir -p ~/.ssh/')
    ssh.exec_command('echo "%s" >> ~/.ssh/authorized_keys')
    ssh.exec_command('chmod 600 ~/.ssh/authorized_keys')
    ssh.exec_command('chmod 700 ~/.ssh/')
    ssh.exec_command('ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -P ""')
    ssh.exec_command('cat ~/.ssh/id_rsa.pub | ssh root@192.168.56.103 %22cat >> ~/.ssh/authorized_keys%22')


    # ftp_client = ssh.open_sftp()
    # ftp_client.get('~./ssh/authorized_keys', "E:/Bash/authorized_keys", 'rw')
    # ftp_client.close()
    # key = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read() #need to seek for remote machine
    # username = os.getlogin()
    # password = getpass()
    #
    #
    # stdin, stdout, stderr = ssh.exec_command("ls /etc/")
    # for line in stdout.readlines():
    #     print line.strip()

    ssh.close()

# ssh.exec_command('cat ~/.ssh/id_rsa.pub | ssh root@192.168.56.101 %22cat >> ~/.ssh/authorized_keys%22')


# for line in file:
#     info = {}
#     info['ip'] = line.split(' ')[0]
#
#     ssh.exec_command('ssh-copy id $USERNAME@')


