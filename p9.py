"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import sys

a = 0
b = 1
c = 2

while(True):
    
    

    b += 1
    c += 1

    a = 1000 - c - b

    print("pp:" + str(a) + "|"+ str(b) + "|"+ str(c) + "|")

    if(True):
        if( (pow(a,2) + pow(b,2)) == pow(c,2) ):      # found result
            print("a: " + str(a))
            print("b: " + str(b))
            print("c: " + str(c))
            sys.exit()

    if(a < 0 or b < 0 or c < 0):
        print("underflow")
        sys.exit()