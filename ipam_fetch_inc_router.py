# info : https://ttl255.com/pynetbox-netbox-python-api-client-p1-getting-info/

""" GET Router List -> DHCP addresses from IPAM """ 

# pip install python-dotenv
import os
import json
from pprint import pprint
import pynetbox
import requests
from dotenv import load_dotenv
load_dotenv()

import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

API_KEY = os.getenv('API_KEY')

url='https://demo.netbox.dev'
token=API_KEY
headers = {
    'accept': 'application/json',
    'Authorization': f'Token {token}',
}

nb = pynetbox.api(url=url, token=token)

def fetch_all_ip_prefixes():
    """ 
    Fetch every ip prefix from IPAM and store in txt file 
    uses pynetbox - evaluate vs standard API 
    """

    with open('ip_address.txt', 'w', encoding='UTF8') as f:
        devices = nb.ipam.prefixes.all()
        for device in devices:
            #print(device.prefix)
            f.write(device.prefix)
            f.write('\n')
        print("done")
        return(len("ip_address.txt"))

def fetch_active_routers():
    """ Standard API syntax """
    response = requests.get(url=url+'/api/dcim/devices/?name__ic=router0',headers=headers,verify=False)

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
