# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 09:30:07 2023

@author: INDIA
"""

'''
line="Horses are taller than dogs."
searchObj=re.search(r'(.*) are (.*?) .*',line,re.M|re.S)
if searchObj:
    print("searchObj.group():",searchObj.group())
    print("searchObj.group(1):",searchObj.group(1))
    print("searchObj.group(2):",searchObj.group(2))
else:
    print("Nothing Found")
'''

import re
line='''Horses are taller than dogs.
 Cats are cuter than dogs.'''
searchObj=re.search(r'(.*) are (.*) .*',line,re.M|re.S)
if searchObj:
    print("searchObj.group():",searchObj.group())
    print("searchObj.group(1):",searchObj.group(1))
    print("searchObj.group(2):",searchObj.group(2))
else:
    print("Nothing Found")
