# a1ce7ad4f0f60ea2bc1a921451583fc85b34c48e
import pynetbox
import time

#It function that connect to netbox and add devices
def adddev(dev):
    nb = pynetbox.api(url='https://demo.netbox.dev/',
                  token='a1ce7ad4f0f60ea2bc1a921451583fc85b34c48e')

    result = nb.dcim.devices.create(
        name=dev,
        device_type=3,
        device_role=4,
        site=4,
    )
    print(result)
#Populate devices in file hosts.txt. 
#Example:
#Device1::192.168.0.1
#Device2::192.168.0.2
#Device2::192.168.0.2
file1 = open('windows-path', 'r')
Lines = file1.readlines()
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    time.sleep(0.5)
    s = line
    l = s.split('::')
    print(l[0])
    dev = l[0]
    adddev(dev)
