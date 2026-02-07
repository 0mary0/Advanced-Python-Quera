p, d = input("Please enter both numbers: ").split()
p = int(p)
d = int(d)
i = 1
while i*d % p > p//2:
    i += 1
print(i*d)