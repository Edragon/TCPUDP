#!/bin/bash
pkill -f "udp_log.py"

rm -rf /var/www/html/server/app2.html

nohup python ~/python_tcp/log/udp_log.py
