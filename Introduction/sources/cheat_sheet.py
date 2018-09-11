# =============== BASE TYPES ==================================
integer = 0
integer = -1
integer = 0b010
integer = 0xF3
float = 0.5
float = .5
float = 1.2e-7
bool = True
bool = False
string = 'this is a string'
string = "this is also a string"
string = """
this is also a string
but this is a multiline string
"""
bytes = b"hey\xfe"

# =============== CONTAINER TYPES =============================
list = [1, "a", '1']
tuple = (1, "a", '1') = 1, "a", '1'
dictionnary = { 'key': 'value', 'a': 1 }
set = { 1, 2, 3, '5' }

# =============== VARIABLES ASSIGNEMENT =======================
y = 5
x = 1.2 + 8 + sin(y)
a, b, c = 1, 2, 3 = (1, 2, 3)
a, b = b, a
x += 1
x -= 1
x *= 1
x /= 1
x = None
del x

# =============== CONVERTIONS ================================
int('15') # = 15
float('11.24e8') # = 1124000000.0
round(15.56, 1) # = 15.6
str(3) # = '3'
list('abc') # = ['a', 'b', 'c']
dict([(key1, val1), (key2, val2)]) # = { key1: val1, key2: val2 }
'abc de'.split() # = ['abc', 'de']
['abc', 'de'].join(' ') # = 'abc de'

# =============== LISTS ======================================
lst = [10, 20, 30, 40, 50]
len(lst) # = 5
lst[0] # = 10
lst[-1] # = 50
lst[1:] # = [20, 30, 40, 50]
lst[:-1] # = [10, 20, 30, 40]
lst[1:-1] # = [20, 30, 40]
lst[::2] # = [10, 20, 30]
lst[::-1] # = [50, 40, 30, 20, 10]
lst[:] # = [10, 20, 30, 40, 50]
lst.sort()
lst.reverse()
lst.append(value)
lst.extend(sequence)
lst.pop()
lst.insert(index, value)

# =============== IF =========================================
if a == b:
    pass
else if a < b:
    a = 1
else if a <= b:
    a = 0
else:
    a = (a >= b)? 1: 0

# =============== FOR ========================================
for i in range(0, 3):
    print(i + ", ")
# 0, 1, 2

while i < a:
    i += 1

# =============== FUNCTION ===================================
def add(arg1, arg2):
    a = arg1 + arg2
    return a

a = add(1, 2) # = 3

# =============== CLASSES ====================================
class Human:
    def __init__(self, name, age):
        assert type(name) == type('')
        assert type(age) == type(1)
        assert len(name) > 0 and age > 0

        self.name = name
        self.age = age

    def __str__(self):
        return 'Name: %s, Age: %d' % (self.name, self.age)

    def say_hi(self):
        return '%s say \'Hi!\' to you' % self.name

david = Human('David', 21)
william = Human('William', 25)

david.name # = William
william.age # = 21

david.say_hi() # David say 'Hi!' to you

# =============== IMPORTS ====================================
import numpy as np
from library import function
from library import *

# =============== READ & WRITE ===============================
with open('file.txt', 'r') as f:
    lines = f.readlines()
    lines = f.readline() # = next line
    char = f.read() # = next char

with open('file.txt', 'w') as f:
    f.write('hey')
    f.writelines(['line1', 'line2'])
