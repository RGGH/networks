# info : https://ttl255.com/pynetbox-netbox-python-api-client-p1-getting-info/

""" GET Router List -> DHCP addresses from IPAM """ 

# https://demo.netbox.dev/

# pip install python-dotenv
import os
import json
from pprint import pprint
import requests

from dotenv import load_dotenv
load_dotenv()

import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

NETBOX_API_TOKEN = os.getenv('NETBOX_API_TOKEN')

NETBOX_API_ROOT = "https://demo.netbox.dev"
NETBOX_DEVICES_ENDPOINT = "/dcim/devices/"
NETBOX_SITES_ENDPOINT = "/dcim/sites/"

token=NETBOX_API_TOKEN

headers = {
    'accept': 'application/json',
    'Authorization': f'Token {token}',
}

# def create_routers():
#     """ for >50 demonstration """
#     json_data = [
#         {

#             "display": "x99",
#             "name": "x99",
#             "device_type": {
#                 "display": "EX9214",
#                 "manufacturer": {
#                     "display": "Juniper",
#                     "name": "Juniper",
#                     "slug": "juniper"
#                 },
#                 "model": "EX9214",
#                 "slug": "ex9214"
#                 }
#         }
        
#     ]

#     response = requests.post('https://demo.netbox.dev/api/dcim/devices/', headers=headers, json=json_data,verify=False)
#     print(response)
    
# def add_devices():
#     parsed_yaml = read_yaml()
#     devices_params_gen = form_device_params_from_yaml(parsed_yaml)
#     for device_params in devices_params_gen:
#         add_device(**device_params)
#     print("All devices have been imported") 'accept': 'application/json',
#     'Authorization': f'Token {token}',
# }

# def create_routers():
#     """ for >50 demonstration """
#     json_data = [
#         {

#             "display": "x99",
#             "name": "x99",
#             "device_type": {
#                 "display": "EX9214",
#                 "manufacturer": {
#                     "display": "Juniper",
#                     "name": "Juniper",
#                     "slug": "juniper"
#                 },
#                 "model": "EX9214",
#                 "slug": "ex9214"
#                 }
#         }
        
#     ]

#     response = requests.post('https://demo.netbox.dev/api/dcim/devices/', headers=headers, json=json_data,verify=False)
#     print(response)
    
# def add_devices():
#     parsed_yaml = read_yaml()
#     devices_params_gen = form_device_params_from_yaml(parsed_yaml)
#     for device_params in devices_params_gen:
#         add_device(**device_params)
#     print("All devices have been imported")


def fetch_active_routers():
    """ Standard API syntax """
    response = requests.get(url=NETBOX_API_ROOT+'/api/dcim/devices/?name__ic=python360',headers=headers,verify=False)
    print(response)

    """ NetBox returns only 50 entities in one response. 
    Make first get request and then make the requests 
    of ‘next’ url in the results until it will be null()."""

    all_results = json.loads(response.text)['results']
    next_url = json.loads(response.text)['next']
    while next_url:
        print(next_url)
        response = requests.get(next_url, headers=headers, verify=False)
        all_results += json.loads(response.text)['results']
        next_url = json.loads(response.text)['next']

    # write output to 'router_list.txt'
    with open('router_list.txt', 'w', encoding='UTF8') as f:

        for router in all_results[:]:
            f.write(str(router))
            f.write('\n')
    
    print("done - check router_list.txt")
    return(len("router_list.txt"))

if __name__ =="__main__":

    fetch_active_routers()
