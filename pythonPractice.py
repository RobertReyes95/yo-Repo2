import os
import sys
import argparse
import re 

foot = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(foot)

 #Testing out the re module,  this takes out duplicates in a sentence
sentence = input('Please enter your sentence here: ')
takeDuplicate = re.sub(r'(\b[a-z]+) \1', r'\1', sentence)
print(takeDuplicate)