# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 08:22:27 2023

@author: INDIA
"""
def stateq0(n):
    if (len(n)==0):
        print("String Accepted")
    else:   
        if(n[0]=='0'):
            stateq0(n[1:])   
        elif (n[0]=='1'):
            stateq1(n[1:])
 
def stateq1(n):
    if (len(n)==0):
        print("String Not Accepted")
    else:   
        if(n[0]=='0'):
            stateq0(n[1:])
        elif (n[0]=='1'):
            stateq1(n[1:])           

n="110"

if len(n)==0:
    print("Insufficiant Data")
else:
    stateq0(n)
    
