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

def generate_string(string, frequency):
    for s in string:
        yield s * frequency


class GenerateString:
    def __init__(self, string, frequency):
       self.string = string
       self.frequency = frequency

    def __iter__(self):
        self.count = -1
        return self

    def __next__(self):
        self.count += 1
        if self.count > len(self.string) - 1:
            raise StopIteration
        return self.string[self.count] * self.frequency


    # Write your code here.

# for i in generate_string("hello", 3):
#     print(i,end="")

genObject = GenerateString("hello", 3)
for g in genObject:
    print(g, end="")