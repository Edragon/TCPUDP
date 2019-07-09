#!/bin/bash
pkill -f "udp_log.py"

rm -rf /var/www/html/tcp/log.html

nohup python ~/TCPUDP/tcp_server_1/main.py
