"""This is an app to Calculate Flying Pay"""

CNRATE1 = 565
CNRATE2 = 1615
CNRATE3 = 2095

FORATE1 = 380
FORATE2 = 1075
FORATE3 = 1410

CNSALARY = 56925
FOSALARY = 36225

CNALLOWANCE = 25000
FOALLOWANCE = 20000

print("Flying Pay Calculator \n")
print("The following are the current rates for CN: ")
print(f"1-50 Hours: ${CNRATE1}/hr")
print(f"51-70 Hours: ${CNRATE2}/hr")
print(f">70 Hours: ${CNRATE3}/hr \n")

print("The following are the current rates for FO: ")
print(f"1-50 Hours: ${FORATE1}/hr")
print(f"51-70 Hours: ${FORATE2}/hr")
print(f">70 Hours: ${FORATE3}/hr \n")

print("The basic salaries for Flight Crew are as follows: ")
print(f"CN: ${CNSALARY}")
print(f"FO: ${FOSALARY} \n")

print("The FIXED allowance for Flight Crew are as follows: ")
print(f"CN: ${CNALLOWANCE}")
print(f"FO: ${FOALLOWANCE} \n")

while True:
    print("What is your rank (Enter 1 or 2)? \n1 - CN \n2 - FO\n")
    RANK = 0
    BASICSALARY = 0
    FIXEDALLOWANCE = 0

    RANK = int(input(": "))
    if RANK == 1:
        BASICSALARY = CNSALARY
        FIXEDALLOWANCE = CNALLOWANCE
    if RANK == 2:
        BASICSALARY = FOSALARY
        FIXEDALLOWANCE = FOALLOWANCE
    else:
        print("Invalid input, please try again.")
        continue

    HOURS = float(input("\nPlease enter how many hours flown: "))

    def allowance(RANK, HOURS):
        if RANK == 1:
            if HOURS <= 50:
                flying_allowance = HOURS * CNRATE1
                return flying_allowance
            if HOURS <= 70:
                flying_allowance = (50 * CNRATE1) + ((HOURS-50) * CNRATE2)
                return flying_allowance
            if HOURS > 70:
                flying_allowance = (50 * CNRATE1) + \
                    (20 * CNRATE2) + ((HOURS-70) * CNRATE3)
                return flying_allowance
        if RANK == 2:
            if HOURS <= 50:
                flying_allowance = HOURS * FORATE1
                return flying_allowance
            if HOURS <= 70:
                flying_allowance = (50 * FORATE1) + ((HOURS-50) * FORATE2)
                return flying_allowance
            if HOURS > 70:
                flying_allowance = (50 * FORATE1) + \
                    (20 * FORATE2) + ((HOURS-70) * FORATE3)
                return flying_allowance

    FLYINGALLOWANCE = int(allowance(RANK, HOURS))

    print(f"Your flying hours for the month is ${FLYINGALLOWANCE}")
    print(
        f"Your total compensation for the month is: ${BASICSALARY+FIXEDALLOWANCE+FLYINGALLOWANCE}")

    QUIT = input("\nPress 'q' or 'Q' to quit, or any key to try again.\n")
    if QUIT.lower() == "q":
        break
