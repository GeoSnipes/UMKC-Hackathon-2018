import json
import os

with open("servers.txt") as server_list:
    servers = json.load(server_list)

print(json.dumps(servers, indent=4))

for node in servers['mail']:
    ssh_string = "ssh geoWe@"+node+" -i ~/.ssh/clab_rsa 'bash -s' < "
    stript_string = "~/UMKC-Hackathon-2018/test.sh"
    pipe_string = " >> 'stdout_"+node+"_'$(date +'%m-%d-%y') 2>> 'stderr_"+node+"_'$(date +'%m-%d-%y')"
    os.system(ssh_string + stript_string + pipe_string)