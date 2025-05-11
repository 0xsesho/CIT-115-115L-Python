#Author: Ethan Boucher
#Class: Py
#Date: 4/25/2025
#Assignment: Paint Job Estimator


#function to get a float input with validation
def getFloatInput(prompt):
    while True:
        try:
            fValue = float(input(prompt + ": "))
            if fValue <= 0:
                print("Value must be greater than zero. Try again.")
                continue
            return fValue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

#calculate gallons of paint required, rounded
import math
def getGallonsOfPaint(fWallSqFt, fFeetPerGallon):
    return math.ceil(fWallSqFt / fFeetPerGallon)

#calculate labor hours required
def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    return fLaborHoursPerGallon * iTotalGallons

#calculate labor cost
def getLaborCost(fLaborHours, fLaborChargePerHour):
    return fLaborHours * fLaborChargePerHour

#calculate paint cost
def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice

#determine sales tax rate based on state
def getSalesTax(sState):
    stateTaxRates = {'CT': 0.06, 'MA': 0.0625, 'ME': 0.085, 'NH': 0.0, 'RI': 0.07, 'VT': 0.06}
    return stateTaxRates.get(sState.upper(), 0.0)

#output results
def showCostEstimate(sCustomerName, sFileName, iGallons, fPaintCost, fLaborHours, fLaborCost, fTaxRate):
    fTotalCost = fPaintCost + fLaborCost
    fTaxAmount = fTotalCost * fTaxRate
    fFinalTotal = fTotalCost + fTaxAmount

    output = (
        f"Customer Last Name: {sCustomerName}\n"
        f"Gallons of paint: {iGallons}\n"
        f"Hours of labor: {fLaborHours:.1f}\n"
        f"Paint charges: ${fPaintCost:.2f}\n"
        f"Labor charges: ${fLaborCost:.2f}\n"
        f"Subtotal: ${fTotalCost:.2f}\n"
        f"Sales tax: ${fTaxAmount:.2f}\n"
        f"Total Cost: ${fFinalTotal:.2f}\n"
    )

    print(output)

    with open(sFileName, "w") as file:
        file.write(output)

    print(f"File '{sFileName}' has been created.")

#main function
def main():
    #get user inputs
    fWallSqFt = getFloatInput("Enter wall space in square feet")
    fPaintPrice = getFloatInput("Enter paint price per gallon")
    fFeetPerGallon = getFloatInput("Enter feet per gallon")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon?")
    fLaborChargePerHour = getFloatInput("Labor charge per hour")

    sState = input("State job is in: ")
    sCustomerName = input("Enter customer's last name: ")

    #calculations
    iGallons = getGallonsOfPaint(fWallSqFt, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iGallons)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iGallons, fPaintPrice)
    fTaxRate = getSalesTax(sState)

    #output
    sFileName = sCustomerName + "_PaintJobOutput.txt"
    showCostEstimate(sCustomerName, sFileName, iGallons, fPaintCost, fLaborHours, fLaborCost, fTaxRate)
if __name__ == "__main__":
    main()