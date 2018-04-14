import json
import sys
import os

# os.chdir(os.path.join(os.path.expanduser('~'), 'UMKC-Hackathon-2018'))
#os.chdir("d:/Users/Geovanni/Sync/Projects/UMKC-Hackathon-2018/")
#with open(sys.argv[1]) as server_list:
# with open("servers.txt") as server_list:
#     # servers = server_list.readlines()
#     servers = json.load(server_list)

# print(servers['mail'])
# print(len(sys.argv))
# print(sys.argv[0])
# print(json.dumps(servers, indent=4))


# os.system("sh test.sh")
# os.system("exec 3>&1 1>file")
# os.system("ssh geoWe@ms0814.utah.cloudlab.us -i ~/.ssh/clab_rsa")
# os.system("hostname")
# os.system("exit")
# # os.system("exec 1>&3 3>&-")
# os.system("exec 2>&1")
# os.system("exec 1>&file")
os.system("ssh geoWe@ms0814.utah.cloudlab.us -i ~/.ssh/clab_rsa 'bash -s' < ~/UMKC-Hackathon-2018/test.sh >> 'stdout_'$(hostname)'_'$(date) 2>>'stderr_'$(hostname)'_'$(date)")