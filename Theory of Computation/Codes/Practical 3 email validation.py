# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 08:21:08 2023

@author: INDIA
"""

import re
email="abc@gmail.com"
searchObj=re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',email)
if searchObj:
    print("This is a Valid Email Address")
else:
    print("Not a Valid Email Address")
