#!/bin/bash
pkill -f "udp_log.py"

rm -rf /var/www/html/server/app2.html

nohup python ~/TCPUDP/udp_server_1/udp_log.py
