''' Tabulate Network Information '''

from ipaddress import IPv4Network, IPv4Interface, IPv4Address
from tabulate import tabulate

vlans = {"sw1": [10, 20, 30, 40], "sw2": [1, 2, 10], "sw3": [1, 2, 3, 4, 5, 10, 11, 12]}
print(tabulate(vlans, headers="keys"))



''' Parse IPv4 Network Information '''

addr = IPv4Address("220.14.9.37")

print(addr)
print(type(addr))


net = IPv4Network("192.4.2.0/24")
print(net.num_addresses)

net = net.netmask
print(net)

ifc = IPv4Interface("192.168.1.6/24")
print(f"ip = {ifc.ip}")
print(f"network = {ifc.network}")

net = IPv4Network("200.100.10.0/24")
for sn in net.subnets(new_prefix=26):
    print(sn)
