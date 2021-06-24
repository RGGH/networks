# -*- coding: utf-8 -*-
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#

import psutil
from tabulate import tabulate
# !pip install psutil
# !pip install tabulate

# credit :  LarsRosenkilde 

class Network_Details(object):

    def __init__(self):
        self.inst = psutil.net_if_addrs()

        """ family: can be either socket.AF_INET, 
        socket.AF_INET6 or psutil.AF_LINK,
        which refers to a MAC address.
        
        Addresses associated to each NIC (network interface card) 
        installed on the system as a dictionary whose keys are the NIC names 
        and value is a list of namedtuples for each address assigned to the NIC"""

    def scanner(self):
        self.interfaces = []
        self.address_ip = []
        self.netmask_ip = []
        self.broadcast_ip = []
        for interface_name, interface_addresses in self.inst.items():
            self.interfaces.append(interface_name)
            for address in interface_addresses:
                if str(address.family) == 'AddressFamily.AF_INET':
                    self.address_ip.append(address.address)
                    self.netmask_ip.append(address.netmask)
                    self.broadcast_ip.append(address.broadcast)

        # create dictionary where values can be a list 
        data = {"Interface"    : [*self.interfaces],
                "IP-Address"   : [*self.address_ip],  
                "Netmask"      : [*self.netmask_ip],
                "Broadcast-IP" : [*self.netmask_ip]
                }

        return tabulate(data, headers="keys", tablefmt="github")
    

    def __str__(self):
        return str(self.scanner())


if __name__ == "__main__":
    print(Network_Details())