import socket
#import threading
import logging

html_str = """
%s
"""

logging.basicConfig(filename='/var/www/html/udp/index.html', filemode='w+', format='%(name)s - %(levelname)s - %(message)s')

log = logging.getLogger('udpx')

log.warning('This will get logged to a file<br>')


bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((bind_ip, bind_port))


print 'Listening on {}:{}'.format(bind_ip, bind_port)

#log.info will not get logged

log.warning("Listening on udp %s:%s <br>" % (bind_port, bind_ip))



while True:
    message, address = server.recvfrom(1024)
	
    print('Received %r from %s' % (message, address))
    
    log.warning('Received %r from %s <br>' % (message, address))
	
    server.sendto("ACK!!", address)
