#! /usr/bin/python2

import socket

			#ipv4		UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#binding ip and port number, it should be a tuple
s.bind(("127.0.0.1",8888))   #receiver's ip, use port >6000, 

while True:
	data= s.recvfrom(1000)
	print "Message...", data[0]
	reply= raw_input("Please enter your reply ")
	s.sendto(reply,data[1])

	
