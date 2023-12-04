# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:55:23 2023

@author: INDIA
"""
count0=0
count1=0

def stateq0(n):    
    if(len(n)==0):
        stateq3()
    else:
        global count0,count1
        if(n[0]=='0'):
            count0=count0+1
            stateq0(n[1:])
        elif(n[0]=='1'): 
            count1=count1+1
            stateq1(n[1:])    

def stateq1(n):
    if(len(n)==0):
       stateq3()
    else:
        global count0,count1
        if(n[0]=='1'):
            count1=count1+1
            stateq1(n[1:])
        elif(n[0]=='0'):
            count0=count0+1
            stateq0(n[1:])      
                  
def stateq3():
    if(count0==count1):
        print("String Accepted");
    else:
        print("String not Accepted ")  

n='10101'

if (len(n)==0):
     print("Insufficient Data...")
elif(n[0]=='0'):
    stateq0(n)
elif (n[0]=='1'):
    stateq1(n) 