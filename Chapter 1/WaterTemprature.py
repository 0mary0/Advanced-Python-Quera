# Problem: Yakhdarchi
# Source: https://quera.org/college/3078/chapter/8407/lesson/29908
# Summary: Determine the physical state of water based on a given temperature in Celsius.
#            - If temperature > 100°C → Steam
#            - If temperature < 0°C   → Ice
#            - Otherwise               → Water
# Approach: Convert input to float, then use conditional statements (if-elif-else) to check ranges
#           and print the corresponding state.
t = input("Enter the tempreture: ")
temp = float(t)
if temp>100:
    print("Steam")
elif temp<0:
    print("Ice")
else:
    print("Water")