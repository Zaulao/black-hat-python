import paramiko

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port, user, passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()

    if output:
        print('--- OUTPUT ---')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    import getpass
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Server IP: ') # or 'static ip adress'
    port = input('Server Port: ') or 2222
    cmd = input('Command: ') or 'id'
    ssh_command(ip, port, user, password, cmd)