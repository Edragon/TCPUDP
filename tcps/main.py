#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import thread
import logging

logging.basicConfig(filename='/var/www/html/tcp/index.html', filemode='w+', format='%(name)s - %(levelname)s - %(message)s')
log = logging.getLogger('tcp')
log.warning('This will get logged to a file<br>')


HOST = ''
PORT = 8100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   ## reuse socket 8100
s.bind((HOST, PORT))
s.listen(5)

print 'Server start at: %s:%s' %(HOST, PORT)
print 'wait for connection...'
log.warning("Listening on udp %s:%s <br>" % (HOST, PORT))



def on_new_client(clientsocket, addr):
    while True:
        data = clientsocket.recv(182).encode('hex') #182

        print codec_data
		
        log.warning('Received %r from %s <br>' % (data, addr))
		
        clientsocket.send("Received at Electrodragon tracker")
        
    clientsocket.close()


    
while True:
    conn, addr = s.accept()
    print 'Connected by ', addr
    thread.start_new_thread(on_new_client, (conn, addr))

