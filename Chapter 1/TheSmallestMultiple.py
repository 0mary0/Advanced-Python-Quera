# Problem: The Smallest Multiple
# Source: https://quera.org/college/3078/chapter/8407/lesson/29915
# Summary: Given two integers p and d, find the smallest multiple of d (i*d) such that
#          the remainder when divided by p is less than or equal to p//2.
# Approach: Start with i = 1 and increment i until (i*d) % p <= p//2. 
#           Once the condition is satisfied, print i*d. The loop is controlled using
#           a while loop with the stopping condition as part of the loop test.
p, d = input("Please enter both numbers: ").split()
p = int(p)
d = int(d)
i = 1
while i*d % p > p//2:
    i += 1
print(i*d)