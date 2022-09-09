# credit : https://ttl255.com/pynetbox-netbox-python-api-client-p1-getting-info/

""" GET Router List -> DHCP addresses from IPAM """ 

# https://demo.netbox.dev/

# pip install python-dotenv
import os
import json
import requests

from dotenv import load_dotenv
load_dotenv()

import pynetbox


import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

NETBOX_API_TOKEN = os.getenv('NETBOX_API_TOKEN')

NETBOX_URL = "https://demo.netbox.dev"
NETBOX_DEVICES_ENDPOINT = "/dcim/devices/"
NETBOX_SITES_ENDPOINT = "/dcim/sites/"

nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_API_TOKEN)


headers = {
    'accept': 'application/json',
    'Authorization': "f'Token {NETBOX_API_TOKEN}}'"
}


# Specify number of Spine and Leaf switches
SPINE_NUM = 20
LEAF_NUM = 80

def bulk_add():
    # List to store dictionaries with attributes for new devices
    p360_devices = []

    # Retrieve objects needed for creation of python360 devices
    site_python360 = nb.dcim.sites.get(slug="python360-dc-01")
    drole_leaf = nb.dcim.device_roles.get(slug="leaf-switch")
    drole_spine = nb.dcim.device_roles.get(slug="spine-switch")
    dtype_ar7060 = nb.dcim.device_types.get(slug="7060cx2-32s")
    dtype_ar7280 = nb.dcim.device_types.get(slug="7280cr2-60")

    # Generate attributes for spines
    for i in range(1, SPINE_NUM + 1):
        p360_devices.append(
            dict(
                name=f"sw-spine-python360-0{i}",
                device_type=dtype_ar7280.id,
                device_role=drole_spine.id,
                site=site_python360.id,
            )
        )

    # Generate attributes for leaves
    for i in range(1, LEAF_NUM + 1):
        p360_devices.append(
            dict(
                name=f"sw-leaf-python360-0{i}",
                device_type=dtype_ar7060.id,
                device_role=drole_leaf.id,
                site=site_python360.id,
            )
        )

    try:
        # Try creating all of the devices at once
        results = nb.dcim.devices.create(p360_devices)

        # Set formatting and header
        fmt = "{:<25}{:<15}{:<15}{:<15}"
        header = ("Device", "Dev Role", "Dev Type", "Site")

        # Print header
        print(fmt.format(*header))

        # Print summary info for each of the devices
        for r in results:
            print(
                fmt.format(
                    r["name"],
                    r["device_role"]["name"],
                    r["device_type"]["model"],
                    r["site"]["name"],
                )
            )

    except pynetbox.RequestError as e:
        return e
    except ValueError as e:
        return e
    
if __name__ =="__main__":
    bulk_add()
