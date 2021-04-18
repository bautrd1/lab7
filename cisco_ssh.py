from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException

USER = input("Please enter your username: ")
PASS = input("Please enter your password: ")

device  = {
    'ip': '192.168.11.11',
    'username': USER,
    'password': PASS,
    'device_type': 'cisco_ios'
}

try:
    c = ConnectHandler(**device)
    output = c.send_command('show run')
    f = open('backup.conf', 'x')
    f.write(str(datetime.now()))
    f.write("\n")
    f.write(output)
    f.close()
except (AuthenticationException):
    print("An authentication error ocurred while connecting to: " + device['ip'])
except (SSHException):
    print("An error ocurred while connecting to device " + device['ip'] + " via SSH")
except (NetMikoTimeoutException):
    print("The device " + device['ip'] + " time out when attempting to connect")
