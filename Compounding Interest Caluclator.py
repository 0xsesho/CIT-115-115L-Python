#Author: :3
#Class: Py
#Date: 4/11/2025
#Assignment: Compounding Interest Calculator w/ loops

#user inputs with validation
while True:
    try:
        fDeposit = float(input("What is the Original Deposit (positive value): "))
        if fDeposit <= 0:
            print("Input must a positive numeric value")
            continue
        break
    except ValueError:
        print("Input must a positive numeric value")

while True:
    try:
        fInterestRate = float(input("What is the Interest Rate (positive value): "))
        if fInterestRate <= 0:
            print("Input must a positive numeric value")
            continue
        break
    except ValueError:
        print("Input must a positive numeric value")

while True:
    try:
        iNumMonths = int(input("What is the Number of Months (positive value): "))
        if iNumMonths <= 0:
            print("Input must a positive numeric value")
            continue
        break
    except ValueError:
        print("Input must a positive numeric value")

while True:
    try:
        fGoal = float(input("What is the Goal Amount (can enter 0 but not negative): "))
        if fGoal < 0:
            print("Input must be 0 or greater")
            continue
        break
    except ValueError:
        print("Input must be 0 or greater")

#convert interest rate
fMonthlyInterestRate = (fInterestRate / 100) / 12

#compound monthly interest calculation
fCurrentBalance = fDeposit
for iMonth in range(1, iNumMonths + 1):
    fInterestEarned = fCurrentBalance * fMonthlyInterestRate
    fCurrentBalance += fInterestEarned
    print(f"Month: {iMonth:<2} Account Balance is: ${fCurrentBalance:,.2f}")

#goal prediction loop
if fGoal > 0:
    fProjectedBalance = fDeposit
    iMonthsToGoal = 0

    while fProjectedBalance < fGoal:
        fProjectedBalance += fProjectedBalance * fMonthlyInterestRate
        iMonthsToGoal += 1
#prints length of time in months to reach goal
    print(f"\nIt will take {iMonthsToGoal:,} months to reach your goal of ${fGoal:,.2f}.")

