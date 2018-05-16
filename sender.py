#! /usr/bin/python2

import socket
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while 3>2:
	s.sendto("HEY!!",("192.168.10.177",9999))
