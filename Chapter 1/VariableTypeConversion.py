# Problem: Variable Type Conversion
# Source: https://quera.org/college/3078/chapter/8407/lesson/29784
# Summary: Read two numbers from input, sum them, and print the integer part of the result.
# Approach: Convert inputs to floats, compute the sum, then cast the sum to an integer before printing.

str1 = input("Enter first number: ")
str2 = input("Enter second number: ")
addition = float(str1) + float(str2)
print(int(addition))