#!m /user/bin/python3

import time
import webbrowser
option='''
Press 1: Enter the data and search Url
Press 2:
Press 3:
Press 4:
Press 5:
Press 6:
Press 7:
'''

print option

ch= raw_input()
webbrowser.open("Hello and welcome")
if ch==1:
	search_data= raw_input("Enter data)
	final_data= search_data.strip()
      #above removing leading and trailing space
	done_data= final_data.split()
      #spliting each word 
	print done_data

