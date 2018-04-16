import json
import os
import sys

with open("/home/geo/.jenkins/workspace/testcloudlab/"+sys.argv[1]) as server_list:
    servers = json.load(server_list)

#print(json.dumps(servers, indent=4))
print(' '.join(servers[sys.argv[2]]))

# below not important in new version, just saved for future reference
if False:
    for node in servers['mail']:
        ssh_string = "ssh geoWe@"+node+" -i /home/geo/.jenkins/workspace/testcloudlab/ssh/id_rsa.pub 'bash -s' < "
        stript_string = "/home/geo/.jenkins/workspace/testcloudlab/test.sh"
        pipe_string = " >> '/home/geo/.jenkins/workspace/testcloudlab/stdout_"+node+"_'$(date +'%m-%d-%y') 2>> '/home/geo/.jenkins/workspace/testcloudlab/stderr_"+node+"_'$(date +'%m-%d-%y')"
        os.system(ssh_string + stript_string + pipe_string)
