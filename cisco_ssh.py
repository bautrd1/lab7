from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

USER = input("Please enter your username: ")
PASS = input("Please enter your password: ")

device  = {
    'ip': '192.168.11.11',
    'username': USER,
    'password': PASS,
    'device_type': 'cisco_ios'
}

c = ConnectHandler(**device)

output = c.send_command('show run')

f = open('backup.conf', 'x')
f.write(str(datetime.now()))
f.write("\n")
f.write(output)
f.close()
