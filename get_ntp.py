# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

from socket import AF_INET, SOCK_DGRAM, socket
from struct import unpack 
from time import ctime

# "https://www.ntppool.org/en/"

def getNTPTime(host = "uk.pool.ntp.org"):

        port = 123
        buf = 2048
        address = (host,port)
        msg = '\x1b' + 47 * '\0'

        # reference time (in seconds since 1900-01-01 00:00:00)
        TIME1970 = 2208988800 # 1970-01-01 00:00:00

        # connect to server
        client = socket( AF_INET, SOCK_DGRAM)
        client.sendto(msg.encode('utf-8'), address)
        msg, address = client.recvfrom( buf )
        t = unpack( "!12I", msg )[10]
        t -= TIME1970
        
        return ctime(t).replace("  "," ")

if __name__ == "__main__":

        print(getNTPTime())
