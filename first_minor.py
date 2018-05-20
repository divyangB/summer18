#!m /user/bin/python3

import time
import webbrowser
import datetime
option='''
Press 1: For search
Press 2: For Image search
Press 3: for url name
Press 4: for current date and time
Press 5: for opening current default browser
Press 6: all ip
Press 7: url and owner info
'''

print (option)

ch= int(raw_input("Enter the choice: "))
#webbrowser.open("Opening browser....")
if ch==1:
	search_data= raw_input("Enter data: ")
	final_data= search_data.strip().split()
     	for i in final_data:
		webbrowser.open_new_tab("https://www.google.com/search?q="+i)

elif ch==2:
	search_data= raw_input("Enter the data to be searched: ")
	final_data= search_data.strip().split()
	for i in final_data:	
		webbrowser.open_new_tab("https://www.google.co.in/search?hl=en&biw=1301&bih=670&tbm=isch&source=hp&biw=&bih=&ei=TiL_WpD2NpjcvQS_zIiYCQ&q="+i)

#elif ch==3:
elif ch==4:
	Time= datetime.datetime.now().time()
	Date= datetime.datetime.now().date()
	print (Time)
	print (Date)

elif ch==5:
	webbrowser.get('firefox').open('https://www.youtube.com/watch?v=AJtDXIazrMo')
