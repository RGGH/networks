# a1ce7ad4f0f60ea2bc1a921451583fc85b34c48e
import pynetbox
import time

nb = pynetbox.api(
    'https://demo.netbox.dev/',

    token='a1ce7ad4f0f60ea2bc1a921451583fc85b34c48e'
)

devices = nb.dcim.devices.all()
for device in devices:
    print(device.name)