# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:22:07 2023

@author: INDIA
"""
#State q0
def stateq0(n):
    if(len(n)==0):
        print("String not Accepted")
    else:
        if(n[0]=='0'):
            stateq0(n[1:])
        elif(n[0]=='1'):
            stateq1(n[1:])
        
#State q1
def stateq1(n):
    if(len(n)==0):
        print("String not Accepted")
    else:
        if(n[0]=='0'):
            stateq2(n[1:])
        elif(n[0]=='1'):
            stateq1(n[1:])
   
#State q2
def stateq2(n):
    if(len(n)==0):
        print("String not Accepted")
    else:
        if(n[0]=='0'):
            stateq0(n[1:])
        elif(n[0]=='1'):
            stateq3(n[1:])
            
#State q3
def stateq3(n):
    if(len(n)==0):
        print("String Accepted")
    else:
        if(n[0]=='0'):
            stateq0(n[1:])
        elif(n[0]=='1'):
            stateq1(n[1:])

re="11101"
stateq0(re)
