# Problem: Hard Calculations
# Source: https://quera.org/college/3078/chapter/8407/lesson/32598
# Summary: Compute the given calculations using the math library
# Approach: Redefine the question using the math library, using different variables for readability

import math
x = int(input("Please enter a number: "))
a = math.ceil(math.pow(x,5/3)+(math.tan(math.radians(x))))
b = math.floor(math.pow(math.pi,2+math.atan(math.pow(math.sin(math.radians(x)),2))))
print (math.gcd(a,b))