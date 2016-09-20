# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:05:27 2016

@author: kasim
"""

x = "{:<6} {:<22} {:<22} {:<22}"

print(x.format('Bytes', 'Largest Unsigned Int', 'Minimun Signed Int', 'Maximum Signed Int'))

b = 1

for num in range (1,5):
    largest = 2**(b*8)
    minim = -2**(b*8-1)
    maxim = 2**(b*8-1)-1
    
    print (x.format(b, largest, minim, maxim ))
    b = b*2  
    
f = ["a","b",123445,"asfdfdfd"]
print(f)

<<<<<<< HEAD
a= [1,2,3,4]
=======
a= [9,8,7,6,5,4,3,2]
>>>>>>> master
print(a)
