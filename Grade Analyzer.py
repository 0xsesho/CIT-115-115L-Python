#Author: Ethan Boucher
#Class: Py (CIT-115-D02)
#Date: 4/5/2025
#Assignment: Grade Analyzer


#prompt for user's name, store in sName var
sName = input("Name of person we are calculating the grades for: ")

#prompt for 4 test scores
intScore1 = int(input("Enter Test Score 1: "))
intScore2 = int(input("Enter Test Score 2: "))
intScore3 = int(input("Enter Test Score 3: "))
intScore4 = int(input("Enter Test Score 4: "))

#ask user if lowest grade should be dropped
sDropLowest = input("Do you want to drop the lowest grade? (Y/N): ").upper()

#validate input for dropping lowest grade
if sDropLowest != "Y" and sDropLowest != "N":
    print("Enter Y or N to drop the lowest Grade. ")
    raise SystemExit

#drop the lowest score/average calculation
if sDropLowest == "Y":
    if intScore1 <= intScore2 and intScore1 <= intScore3 and intScore1 <= intScore4:
        fAverage = (intScore2 + intScore3 + intScore4) / 3
    elif intScore2 <= intScore1 and intScore2 <= intScore3 and intScore2 <= intScore4:
        fAverage = (intScore1 + intScore3 + intScore4) / 3
    elif intScore3 <= intScore1 and intScore3 <= intScore2 and intScore3 <=intScore4:
        fAverage = (intScore1 + intScore2 + intScore4) / 3
    else:
        fAverage = (intScore1 + intScore2 + intScore3) / 3
else:
    fAverage = (intScore1 + intScore2 + intScore3 + intScore4) / 4

#calulate letter grade
if fAverage >= 97.0:
    sLetterGrade = "A+"
elif fAverage >= 94.0:
    sLetterGrade = "A"
elif fAverage >= 90.9:
    sLetterGrade = "A-"
elif fAverage >= 87.0:
    sLetterGrade = "B+"
elif fAverage >= 84.0:
    sLetterGrade = "B"
elif fAverage >= 80.0:
    sLetterGrade = "B-"
elif fAverage >= 77.0:
    sLetterGrade = "C+"
elif fAverage >= 74.0:
    sLetterGrade = "C"
elif fAverage >= 70.0:
    sLetterGrade = "C-"
elif fAverage >= 67.0:
    sLetterGrade = "D+"
elif fAverage >= 64.0:
    sLetterGrade = "D"
elif fAverage >= 60.0:
    sLetterGrade = "D-"
else:
    sLetterGrade = "F"

#check for scores less than 0, if found prints string and exits
if intScore1 < 0 or intScore2 < 0 or intScore3 < 0 or intScore4 < 0:
    print("Test scores must be greater than 0")
    raise SystemExit

#output results, letter grade and average of grades
print(f"{sName}'s test average is: {fAverage:.1f}")
print(f"Letter Grade for the test is: {sLetterGrade}")

