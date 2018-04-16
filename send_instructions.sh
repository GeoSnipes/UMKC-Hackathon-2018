#!/bin/bash          
server=$(python3 server-to-json.py servers.txt mail)
for p in $server; do
    echo $p
    (ssh "geoWe@"$p "bash -s" < ./test.sh 1&>> ./stdout_$p$(date +"%m-%d-%y")) &
done

FAIL=0
for job in `jobs -p`
do
wait ${job} || FAIL=$((FAIL+1))
done

if [ "$FAIL" == "0" ];
then
else
echo "FAIL! ($FAIL)"
fi
