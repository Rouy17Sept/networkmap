import socket
import subprocess

network_prefix = '???.???.???.'
devices_found = []

for i in range(1, 255):
    ip_address = network_prefix + str(i)
    response = subprocess.call(['ping', '-n', '1', '-w', '500', ip_address])
    if response == 0:
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
        except:
            hostname = "Unknown"
        devices_found.append("{} ({})".format(ip_address, hostname))

with open('devices.txt', 'w') as f:
    for device in devices_found:
        f.write(device + '\n')

print("Found {} devices. Results saved to devices.txt".format(len(devices_found)))
