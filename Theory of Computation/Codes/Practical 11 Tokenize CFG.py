# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 07:54:29 2023

@author: INDIA
"""
import nltk
from nltk import tokenize
grammer1=nltk.CFG.fromstring("""
S -> VP
VP -> VP NP
NP -> Det NP
Det -> 'that'
NP -> singular Noun
NP -> 'fight'
VP -> 'Book'                             
""")
sentence="Book that fight"
for index in range(len(sentence)):
    all_tokens=tokenize.word_tokenize(sentence)
    print(all_tokens)
parser=nltk.ChartParser(grammer1)
for tree in parser.parse(all_tokens):
    print(tree)
    tree.draw()