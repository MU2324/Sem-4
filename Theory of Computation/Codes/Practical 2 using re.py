# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:41:05 2022

@author: INDIA
"""

import re
'''
#Searching
x="A regular expression (shortened as regex or regexp; sometimes referred to as rational expression) is a sequence of characters that specifies a search pattern in text. Usually such patterns are used by string-searching algorithms for 'find' or 'find and replace' operations on strings, or for input validation. Regular expression techniques are developed in theoretical computer science and formal language theory."
if re.search("the",x):
    print("Search Completed for 'the'")
 

#findall
x="A regular expression (shortened as regex or regexp; sometimes referred to as rational expression) is a sequence of characters that specifies a search pattern in text. Usually such patterns are used by string-searching algorithms for 'find' or 'find and replace' operations on strings, or for input validation. Regular expression techniques are developed in theoretical computer science and formal language theory."
s1=re.findall("the",x)
for i in s1:
    print(i)


#Iterator Strating and Ending
x="A regular expression (shortened as regex or regexp; sometimes referred to as rational expression) is a sequence of characters that specifies a search pattern in text. Usually such patterns are used by string-searching algorithms for 'find' or 'find and replace' operations on strings, or for input validation. Regular expression techniques are developed in theoretical computer science and formal language theory." 
for i in re.finditer("the",x):
    s2=i.span()
    print(s2)

  
#Match words with particular pattern
x="ran ban can man"
s3=re.findall("[rbcm]an",x)
for i in s3:
    print(i)
  

#Match series of range of characters
x="ran ban can man"
s4=re.findall("[d-z]an",x)
for i in s4:
    print(i)
 

#Except the Symbols
x="ran ban can man"
s5=re.findall("[^b-p]an",x)
for i in s5:
    print(i)


#Replace string
x="ran ban can man"
s6=re.compile("[b]an")
r=s6.sub("tan",x)
print(r)


#Replace new line with space
x="""ran ban can man
stan"""
s7=re.compile("\n")
r=s7.sub(" ",x)
print(r)


#match character
x="1234WXY8Z"
s8=re.findall("\d",x)
print(s8)
s8=len(re.findall("\d",x))
print(s8)
'''

#Multiple matches
x="12 123 1234 12345 123456 1234567"
s9=re.findall("\d{5,7}",x)
print(s9)
s9=len(re.findall("\d{5,7}",x))
print(s9)
