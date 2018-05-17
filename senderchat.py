#! /usr/bin/python2
import socket,time
import numpy


s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
a=[]
msg=[]
while 2>1:
	msg=a.append()
	msg=raw_input("Enter the message to send: ")
	s.sendto(msg,("127.0.0.1",8888))
	a=s.recvfrom(100)
 	print a

final_msg= msg.strip().split()

print final_msg
