"""This is a Flying Allowance Calculator App"""
print("Flying Allowance Calculator \n")
print("The following are the current rates: ")
print("1-50 Hours: $360/hr")
print("51-70 Hours: $1015/hr")
print(">70 Hours: $1355/hr")

RATE1 = 360
RATE2 = 1015
RATE3 = 1355

HOURS = float(input("\nPlease enter how many hours flown: "))

if HOURS <= 50:
    print(f"You should get ${HOURS * RATE1} in allowance.")
elif HOURS <= 70:
    print(f"You should get ${(50 * RATE1) + ((HOURS-50) * RATE2)} in allowance.")
elif HOURS > 70:
    print(f"You should get ${(50 * RATE1) + (20 * RATE2) + ((HOURS-70) * RATE3)} in allowance.")