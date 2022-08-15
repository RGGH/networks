import requests
from pprint import pprint

headers = {
    'Authorization': 'Token a1ce7ad4f0f60ea2bc1a921451583fc85b34c48e',
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
    'Accept': 'application/json',
}

json_data = {
    'query': 'query {circuit_list(status:"active") {cid provider {name}}}',
}

response = requests.post('https://demo.netbox.dev/graphql/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"query": "query {circuit_list(status:\\"active\\") {cid provider {name}}}"}'
#response = requests.post('https://demo.netbox.dev/graphql/', headers=headers, data=data)

pprint(response.content)
