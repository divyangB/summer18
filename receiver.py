#! /usr/bin/python2

#chat application code by using socket programming 
#use port number> 6000
#we are not using any standard protocol

import socket

rec_ip= "192.168.10.177"
myport = 9999


#this coding is only for receiver, SOCK_STREAM for TCP
#		ipv4	     , for UDP protocol

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Now connecting ip and port

s.bind((rec_ip,myport))

#if net is off only sender can send but we cant't receive, 2 is the length of the message or buffer size

#while condition is true , it will run lifetime

while 4>2:
	print  s.recvfrom(10)




