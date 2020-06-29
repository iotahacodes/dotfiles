#!/bin/python

def is_prime(num):
    res = True

    if(num == 1 or num == 0):
        res = False
        return res

    for i in range(2, num):
        if(num % i == 0):
            res = False
    return res


count = 0
for x in range(10000, 1000000000):
    if(is_prime(x)):
        count += 1
print(count)
