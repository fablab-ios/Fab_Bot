#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:56:38 2019

@author: dishenghuang
"""

import imaplib
#import pprint
#import email

imap_host = 'imap.uvm.edu'
imap_user = 'fabapp@uvm.edu'
imap_pass = 'g00dTick3ts19'

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host,993)

## login to server
imap.login(imap_user, imap_pass)

imap.select('Inbox')

tmp, data = imap.search(None, 'ALL')


for num in data[0].split():
    tmp, data = imap.fetch(num, '(RFC822)')
    #print('Message: {0}\n'.format(num))
    #pprint.pprint(data[0][1])
    #print()
    #print(data[0][1].decode("utf-8"))
    #print(data[0][1].decode("utf-8"))
    #print()
    #filter the email
    if "UVM FabLab" in data[0][1].decode("utf-8"):
        try:
            #ticket name
            print("ticket name: "+ data[0][1].decode("utf-8").split("Student ID:")[0].split("&nbsp; ")[1].split("</pre>")[0].replace("=","") .replace('\r\n',''))
            #print("-------------------------------------------")
            #ticket number
            print("ticket number: "+ data[0][1].decode("utf-8").split("Student ID:")[0].split("Ticket Number:</b>&nbsp; ")[1].split("</pre>")[0])
            #filter the student id 
            print("student id: " + data[0][1].decode("utf-8").split("Student ID:")[1].split("</pre>")[0])
            #filter the status
            print("status: " + data[0][1].decode("utf-8").split("Student ID:")[1].split("</pre>")[1].split("&nbsp; ")[1])
            #filter the date, the time, and the name
            date_split = data[0][1].decode("utf-8").split("Student ID:")[1].split("<i>")[1].split(":</i>")[0].split("on ")
            date =  date_split[1].split(" ")
            print("The date: "+ date[0])
            print("The time: "+ date[2])
            name = data[0][1].decode("utf-8").split("Student ID:")[1].split("<i>")[1].split(":</i>")[0].split("by ")
            print("The name: " + name[1])
            #description
            print("description: " + data[0][1].decode("utf-8").split("Student ID:")[1].split("<i>")[1].split(":</i><br>\r\n")[1].split("<br>")[0])
        except IndexError:
            continue
    #print(email.message_from_bytes(data[0][1]))
    #print()
    
    
imap.close()

