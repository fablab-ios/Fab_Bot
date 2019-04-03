#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:56:38 2019

@author: dishenghuang
"""

import imaplib
import pprint
import email

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
    print('Message: {0}\n'.format(num))
    #pprint.pprint(data[0][1])
    print(email.message_from_bytes(data[0][1]))
    
imap.close()

