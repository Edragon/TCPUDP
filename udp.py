import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((bind_ip, bind_port))


print 'Listening on {}:{}'.format(bind_ip, bind_port)



while True:
    message, address = server.recvfrom(1024)
    print('Received %r from %s' % (message, address))
	
    server.sendto("ACK!!", address)
