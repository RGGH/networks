# -*- coding: utf-8 -*-
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#

interfaces = [1,2,3]
        
# create dictionary where values can be a variable length list 
data = {"Interface" : [*interfaces] }

#print(data.values())

print(type(data['Interface']))