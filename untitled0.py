#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:18:45 2019

@author: dishenghuang
"""
#input("Can I get your email adress? ")

import datetime

class bot:  
    
    def __init__(self):
        self.email = input("Can I get your email adress? ")
        self.create_date = datetime.date.today()
        self.ticket_number = "01"
        self.student_id = "007"
        
    def tracking_create(self):
        print(datetime.date.today() - self.create_date)
        
    def start(self):
        print("For student : {}".format(self.student_id))
        print("Your ticket number is {}".format(self.ticket_number))
        print("We start to process your application.")
    
    def processing(self):
        print("For student : {}".format(self.student_id))
        print("Your ticket number is {}".format(self.ticket_number))
        print("We are still processing your application.")
        
    def finish(self):
        print("For student : {}".format(self.student_id))
        print("Your ticket number is {}".format(self.ticket_number))
        print("We have finished your application.")


      
a = 1
b = str(a)
print("how are you?" + b)
        
        
        
        
        
"""
import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())
"""