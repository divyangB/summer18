#! /usr/bin/python2

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("127.0.0.1",8888))

while 2>1:
	data= s.recvfrom(1000)
	print "Data from client: ", data[0]
	reply= raw_input("Please enter your reply ")
	s.sendto(reply,data[1])
