from ipaddress import IPv4Address

addr = IPv4Address("220.14.9.37")

print(addr)
print(type(addr))


from ipaddress import IPv4Network
net = IPv4Network("192.4.2.0/24")
print(net.num_addresses)

net = net.netmask
print(net)

from ipaddress import IPv4Interface
ifc = IPv4Interface("192.168.1.6/24")
print(f"ip = {ifc.ip}")
print(f"network = {ifc.network}")

net = IPv4Network("200.100.10.0/24")
for sn in net.subnets(new_prefix=26):
    print(sn)
