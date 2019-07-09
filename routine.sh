#!/bin/bash
pkill -f "/root/TCPUDP/tcps/main.py"

rm -rf /var/www/html/tcp/index.html

nohup python /root/TCPUDP/tcps/main.py &
