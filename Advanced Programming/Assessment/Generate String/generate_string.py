"""
Generate String

Write a generator that accepts a string and an integer called frequency
and generates a sequence as follows:
string[0] * frequency + string[1] * frequency + ... + string[-1] + frequency
Your generator should *not* store this string, it should generate the next 
element in the sequence each time its next method is called.

You should create this generator in both a functional and class based way. 
Your functional generator should be named generate_string and your class
based generator (a.k.a iterator) should be named GenerateString.

You may assume that frequency >= 0
"""