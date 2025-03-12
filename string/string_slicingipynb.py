# -*- coding: utf-8 -*-
"""String_slicingipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g6k9H8a2ZdwSGYA7A4UKrt2rKqc8V3Q3

#String Slicing
"""

s = "Hello, Python!"
s2=s[1:4]
print(s2)

#Retrieve All Characters
s = "Hello, Python!"
s2=s[0:]
print(s2)

s3=s[::]
s3

print(s[3:])

s = "abcdefghi"

# Every second character
print(s[::3])

# Every third character from index 1 to 8 (exclusive)
print(s[1:8:3])

#extract neg values
s = "abcdefghijklmno"

# Characters from index -4 to the end
print(s[-4:])

# Characters from the start up to index -3 (excluding -3)
print(s[:-3])

# Characters from index -5 to -2 (excluding -2)
print(s[-5:-2])

# Get every 2nd elements from index -8 to -1 (excluding index -1)
print(s[-8:-1:2])

s = "Python"

# Reverse the string
print(s[::-1])

def reverse_string(str):
    return ' '.join(reversed(str))
s = "Python love"

# Reverse the string
print(reverse_string(s))

"""#f-strings in Python"""

# Python3 program introducing f-string
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")


name = 'Om'
age = 22
print(f"Hello, My name is {name} and I'm {age} years old.")

import datetime
s=datetime.datetime.now()
print(f"{s:%d-%m-%Y}")

"""#Printing Dictionaries key-value using f-string in Python"""

Geek = { 'Id': 112,
         'Name': 'Harsh'}

print(f"Id of {Geek['Name']} is {Geek['Id']}")

