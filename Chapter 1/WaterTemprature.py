t = input("Enter the tempreture: ")
temp = float(t)
if temp>100:
    print("Steam")
elif temp<0:
    print("Ice")
else:
    print("Water")