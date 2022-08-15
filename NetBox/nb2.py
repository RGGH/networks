import requests
import json
import urllib

headers = {
    'Authorization': 'Token a1ce7ad4f0f60ea2bc1a921451583fc85b34c48e',
}


subnet = "172.16.0.1/24"

response = requests.get('https://demo.netbox.dev:443/api/ipam/ip-addresses/?q=&parent=' + str((subnet)), headers=headers, verify=False)
print(response.content)
all_results = json.loads(response.text)['results']
next_url = json.loads(response.text)['next']
while next_url:
    print(next_url)
    response = requests.get(next_url, headers=headers, verify=False)
    all_results += json.loads(response.text)['results']
    next_url = json.loads(response.text)['next']


print(all_results[0])