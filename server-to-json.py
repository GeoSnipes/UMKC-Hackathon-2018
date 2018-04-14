import json
import sys
from os import chdir

chdir("d:\\Users\\Geovanni\\Sync\\Projects\\UMKC-Hackathon-2018\\")

with open("servers.txt") as server_list:
    # servers = server_list.readlines()
    servers = json.load(server_list)

print(servers['mail'])
print(len(sys.argv))
print(sys.argv[0])
#print(json.dumps(servers, indent=2))