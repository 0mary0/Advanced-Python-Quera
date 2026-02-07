# Problem: Multiplication Table
# Source: https://quera.org/college/3078/chapter/8407/lesson/29912
# Summary: Given an integer n, print the n × n multiplication table.
# Approach: Use two nested loops: the outer loop iterates over rows (1 to n),
#           the inner loop iterates over columns (1 to n) and prints the product
#           of the current row and column, formatted with a space. Print a newline
#           after each row.
num = int(input("Enter the number: "))
for i in range(1,num+1):
    for j in range(1,num+1):
        print(i*j, end=" ")
    print("\n")