# coding:utf-8
# The proposal of the exercice is to calculate the volume of a right cone for any radius r and any height h.

from math import *

print ("The proposal of the exercice is to calculate the volume of a right cone for any radius r and any height h")

def input_value(x):
    a = x
    x = -1
    while x < 0 :
        try :
            x = float(input(str(a) +" must be positive. Let's have "+ str(a) +" = "))  
        except ValueError :
            print(str(a), "must be a positive float number ;) Try again...")
    return x

r = "r"
h = "h"
r = input_value(r)
h = input_value(h)

volume = pi * r**2 * h / 3

print("the volume of a cone with a radius of " + str(r) + "m and with a height of " + str(h) + "m is " + str(volume) + "m3.")
