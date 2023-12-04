# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 08:46:00 2022

@author: INDIA
"""
import re
'''
#phone number
x="9420258942"
if re.search("[89][0-9]{,9}",x):
    print("It is a phone number")

#email 
x="PQR_789@gmail.in"
if re.search("[a-zA-Z0-9_\-\.]+@[a-z]+[\.][com|in]{2,3}",x):
    print("It is am Email ID")

#Date
x="20-06-2003"
if re.search("\d{,2}-\d{,2}-\d{,4}",x):
    print("This is a Valid Date")
'''

#Strings
x="Sanika"
if re.search("[a-zA-Z][^\d]",x):
    print("This is a valid String")
