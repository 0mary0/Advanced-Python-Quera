# Problem: Combinations Function
# Source: https://quera.org/college/3078/chapter/8407/lesson/32597
# Summary: Compute the binomial coefficient C(n, k), i.e., the number of ways
#          to choose k elements from n elements efficiently.
# Approach: 
#   - Handle invalid k values (k < 0 or k > n) by returning 0.
#   - Use symmetry property C(n, k) = C(n, n-k) to minimize iterations.
#   - Compute the result iteratively using the multiplicative formula:
#       result = product of (n-i+1)/i for i from 1 to k.
#   - Return the integer result directly, avoiding factorial calculations.

def comb(n, k):
    if k < 0 or k > n:
        return 0
    
    k = min(k, n - k)
    result = 1
    
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    
    return result