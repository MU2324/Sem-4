# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 09:42:09 2022

@author: INDIA
"""

import nltk
data="Hello, I am Sanika Munankar, and I will be completing my bachelor’s degree in Computer Science from SRM College. I have worked on a wide variety of projects that have allowed me to put what I’ve learned in the classroom into use in a practical sense.  I pride myself on being detail-oriented, analytical, and driven."
token=nltk.sent_tokenize(data)
print(token)

tokenw=nltk.word_tokenize(data)
print(tokenw)
