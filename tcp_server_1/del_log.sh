#!/bin/bash
pkill -f "/var/www/html/tcp/main.py"

rm -rf /var/www/html/tcp/log.html

nohup python ~/TCPUDP/tcp_server_1/main.py &
