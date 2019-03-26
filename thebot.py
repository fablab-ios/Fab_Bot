#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:27:08 2019

@author: dishenghuang
"""

import sqlite3 as lite

def read_file(path):
    inf = {}
    with open(path, 'r') as file:
        x = file.readlines()
    #Get the current date
    current_date = x[2].replace("Date", "")
    current_date = current_date.replace("\n","")
    current_date = current_date.replace(":","")
    inf['date'] = current_date.lstrip()
    #Get the enter date
    enter_date = x[12].split("by")
    inf['enter date'] = enter_date[0].rstrip()
    #Student Name
    st_name = enter_date[1]
    st_name = st_name.replace(":\n","")
    inf['Student Name'] = st_name.lstrip()
    #Get the ticket name
    ticket_name = x[7].replace(" Ticket Name:","")
    ticket_name = ticket_name.replace("\n","")
    ticket_name = ticket_name.replace("'"," ")
    ticket_name = ticket_name.lstrip()
    inf['ticket name'] = ticket_name
    #Get the ticket number
    ticket_number = x[8].replace("Ticket Number:","")
    ticket_number = ticket_number.replace("\n","")
    inf['ticket number'] = ticket_number.lstrip()
    #Get the status
    stat = x[10].replace("Status:","")
    stat = stat.replace("\n","")
    inf['status'] = stat.lstrip()
    return inf

print(read_file("closed.txt"))
print(read_file("pickup.txt"))
print(read_file("waiting.txt"))
closed = read_file("pickup.txt")


con = lite.connect('user.db')


with con:
    cur = con.cursor()    
    cur.execute("CREATE TABLE Users(date TEXT, 'enter date' TEXT, 'student name' TEXT, 'ticket name' TEXT, 'ticket number' TEXT, status TEXT)")
    #cur.execute("CREATE TABLE Users(date TEXT)")
    #cur.execute("INSERT INTO Users VALUES(1,'Michelle')")
    cur.execute("INSERT INTO Users VALUES('"+ closed['date'] + "','"+closed['enter date']+"','"+closed['Student Name']+"','"+closed['ticket name']+"','"+ closed['ticket number'] + "','" + closed['status']+"')")

with con:
    cur = con.cursor()    
    cur.execute("SELECT * FROM Users")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
        
  
    
    
    
    
