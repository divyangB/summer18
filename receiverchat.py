#! /usr/bin/python2

import socket

a=['hi','hello','yo']
global hello_count
global hi_count 


def count(a):
	hello_count = 0
	hi_count = 0
	
	for i in range(0, (len(a))):
		if a[i]=="hi":
			hi_count= hi_count+1
		elif a[i]=="hello":
			hello_count= hello_count+1
	print str(hello_count)
	print str(hi_count)


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("127.0.0.1",8888))

while 2>1:
	data= s.recvfrom(1000)
	print "Data from client: ", data[0]
	count(a)
	#reply= raw_input("Please enter your reply ")
	#s.sendto(reply,data[1])

	
