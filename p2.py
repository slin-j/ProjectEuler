"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Lösung:
4613732
"""

import math



val_old = 1
val = 2
sum = 2 # start at 2 cuz val starts at an even number 2

while True:   
    calc = val_old + val    #new fibo number
    
    if calc > 4500000:  # while smaller than highest fibonacci value
        break

    if (calc % 2) == 0:  # if even and not odd
        sum += calc

    val_old = val   # shift by 1 position
    val = calc

print(str(sum))