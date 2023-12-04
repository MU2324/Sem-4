# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 08:51:56 2023

@author: INDIA
"""
def stateq0(n):
    if (len(n)==0):
        print("String Accepted")
    else:   
        if(n[0]=='0' or n[0]=='2' or n[0]=='4' or n[0]=='6' or n[0]=='8'):
            stateq0(n[1:])   
        elif (n[0]=='1' or n[0]=='3' or n[0]=='5' or n[0]=='7' or n[0]=='9'):
            stateq1(n[1:])
 
def stateq1(n):
    if (len(n)==0):
        print("String Not Accepted")
    else:   
        if(n[0]=='0' or n[0]=='2' or n[0]=='4' or n[0]=='6' or n[0]=='8'):
            stateq0(n[1:])   
        elif (n[0]=='1' or n[0]=='3' or n[0]=='5' or n[0]=='7' or n[0]=='9'):
            stateq1(n[1:])           
          
n="4546"

if len(n)==0:
    print("Insufficiant Data")
else:
    stateq0(n)
    
    