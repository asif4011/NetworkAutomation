from netmiko import ConnectHandler # Module which enables SSH connection
platform = 'cisco_ios'

device = ConnectHandler(device_type=platform, ip='192.168.3.2', username='admin', password='admin')
device.find_prompt()



output = device.send_command("ping 192.168.3.1")
print(output)
device.disconnect()