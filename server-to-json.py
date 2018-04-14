import json
import sys
from os import chdir

chdir("~/UMKC-Hackathon-2018")

#with open(sys.argv[1]) as server_list:
with open("servers.txt") as server_list:
    # servers = server_list.readlines()
    servers = json.load(server_list)

print(servers['mail'])
print(len(sys.argv))
print(sys.argv[0])