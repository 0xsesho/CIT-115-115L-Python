#Class: Py (CIT-115-D02)
#Date: 3/1/2025
#Assignment: Compound Interest Calculator


#Input
fPrincipal_Value = float(input("Enter the starting principal: ")) #prompts user for input of principal, converts to float & assigns to variable
fAnnual_Interest = float(input("Enter the annual interest rate: ")) #prompts user for input of annual interest, converts to float & assigns to variable
fC_Interest = float(input("How many times per year is the interest compounded?: ")) #prompts user for input of compound interest, converts to float & assigns to variable
fYears= float(input("For how many years will the account earn interest?: ")) #prompts user for input of number of years, converts to float & assigns to variable

##Calculation
r = fAnnual_Interest / 100 #divides fAnnual_Interest by 100 and assigns to r variable
m = fC_Interest #assigns fC_Interest to m variable
t = fYears #assigns fYears to t variable
#Formula: FV = PV(1 + r/m)^mt
fFuture_Value = fPrincipal_Value * ((1 + r/m) ** (m * t)) #assigns the value of completed calculation based on the formula commented above to fFuture_Value

#Output
print(f"At the end of {int(fYears)} years you will have ${fFuture_Value:,.2f}")#prints string with fYears variable as an int, formatted fFuture_Value with 2 decimal points
