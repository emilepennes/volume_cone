# coding:utf-8
"""The proposal of the exercice is to calculate
the volume of a right cone for any radius R and any height H.
"""

from math import pi

print("The proposal of the exercice is to calculate" +
      "the volume of a right cone for any radius R and any height H")

def input_value(x):
    """Input a positive float value"""
    a = x
    x = -1
    while x < 0:
        try:
            x = float(input(str(a) +" must be positive. Let's have "+ str(a) +" = "))
        except ValueError:
            print(str(a), "must be a positive float number ;) Try again...")
    return x

R = "R"
H = "H"
R = input_value(R)
H = input_value(H)

VOLUME = pi * R**2 * H / 3
VOLUME_ROUND = round(VOLUME, 2)

print("the volume of a cone with a radius of " + str(R) + "m and with a height of " +
      str(H) + "m is " + str(VOLUME_ROUND) + "m3.")
      
