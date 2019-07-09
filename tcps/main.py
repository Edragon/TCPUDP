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

        print data
		
	if data[0:4] == '7e7e':
		#print ("ED20 GPS Tracker: star_char-%s, version-%s, action-%s, pack_times-%s" % (data[0:4], data[4:12], data[12:16], data[16:20]) ) # simple print demo
		log.warning('ED20 GPS Tracker Brief: star_char-%s, version-%s, action-%s, pack_times-%s  <br>' % (data[0:4], data[4:12], data[12:16], data[16:20])   )
		
		log.warning('ED20 GPS Tracker SN: Time-%s, ID-%s, SN-%s  <br>' % (data[20:32], data[74:86], data[44:56])   )
		
		log.warning('ED20 GPS Tracker GPS Data: type- %s, :LOG-%s, LAT-%s  <br>' % (data[106:114], data[114:122], data[122:130])   )
		
		log.warning('ED20 GPS Tracker Full Data %r from %s <br>' % (data, addr))
		
		clientsocket.send("Received at Electrodragon tracker")
		
        else:
	    	log.warning('Received TCP Random Data %r from %s <br>' % (data, addr))
		
		
    clientsocket.close()


    
while True:
    conn, addr = s.accept()
    print 'Connected by ', addr
    thread.start_new_thread(on_new_client, (conn, addr))

