# UMKC Hackathon 2018

<h3>Prerequisites:</h3>
<pre>
*Python installed
*Instructions to forward to servers on system
*List of servers stored as json
*Server keys already installed</pre>

<h3>Instructions</h3>
<pre>
*in send_instructions.sh, change servers.txt to json formatted list of servers
*Change mail to the cluster of servers to be updated
<br>
Thats it, run command</pre>

<h3>Code flow:</h3>
<pre>
*Line 2 takes the arguments and uses python to return only the server cluster requested
*Line 5 then ssh into each server and passes the test.sh file which contains the script to be run in parallel</pre>

<h3>Note:</h3>
<pre>
*It also pipes back the output of each server into its own log file
*If any error occurs on each server, it will output the value on how many servers it occurs</pre>

<h3>Future Work:</h3>
<pre>Dynamically get files from per se git</pre>
