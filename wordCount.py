#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:39:10 2020

@author: williamcroslen
"""

#! /usr/bin/env python3

import sys        # command line arguments
import os         # checking if file exists

# set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]
word_count = {}

#make sure text files exist
if not os.path.exists(textFname):
    print ("text file input %s doesn't exist! Exiting" % textFname)
    exit()

file = open(textFname, 'r') 
Lines = file.readlines() 
  
def remove_special(string): #return list of words without special characters
    a = []
    for i in range(len(string)):
        if not string[i].isalpha():
            string = string[:i] + " " + string[i+1:]
            a = string.split(" ")
    return a
            
def add_to_dict(word):
    word = str(word)
    if (word in word_count):
            word_count[word] +=1
    else:
            word_count[word] = 1
    
    
for line in Lines: 
    line=line.strip() #remove '\n'
    each = line.split(" ")
    for word in each:
        word = word.lower()
        if not word.isalpha(): #if word has special characters
            words = remove_special(word)
            for i in range(len(words)):
                if words[i] == None:
                    continue
                if not words[i].isalpha():
                    continue
                add_to_dict(words[i])
        if not word.isalpha():
            continue
        add_to_dict(word)
        
sorted_dict = sorted(word_count) #alphabatize dict

with open(outputFname, 'w') as writer:
    for i in sorted_dict:
        ans = i + " " + str(word_count[i]) + "\n"
        writer.write(ans)

