#! /usr/bin/python2

import socket

#create a socket argument s
			#ipv4 		udp
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
	msg = raw_input("Enter your message:  ")
	s.sendto(msg,("127.0.0.1",8888))
	reply = s.recvfrom(1000)
	print "Message...",reply[0]
