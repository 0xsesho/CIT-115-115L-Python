#Author: Ethan Boucher
#Class: Py (CIT-115-D02)
#Date: 3/20/2025 - 3/23/2025
#Assignment: Temperature Converter


#welcome message
sName = "Ethan"
print(f"{sName}'s Temperature Converter:")

#user input
fTemp = float(input("Enter a temperature: ")) #prompts user for temp
sScale = input("Is the temp F for Fahrenheit or C for Celsius? ").upper() #prompts user for F or C, if user enters lowercase it is converted to uppercase

#validate user input
if sScale not in ('F', 'C'): #if sScale isn't F/f or C/c,
    print("Enter an F or C") #displays "enter an F or C" and ends program
else:
    if sScale == 'F': #if sScale is F
        if fTemp > 212: #checks if fTemp is greater than 212 F
            print("Temp can not be > 212") #if it is, prints error string and ends program
        else:
            fCelsius = (5.0 / 9) * (fTemp - 32) # if it isn't over 212 F, calculate for F to C | (Celsius = (5.0 / 9) * (USER ENTERED TEMP – 32)
            print(f"The Celsius equivalent is: {fCelsius:.1f}") #prints F to C conversion, formatted to 1 decimal point
    elif sScale == 'C': #if sScale is C
        if fTemp > 100: #checks if fTemp is greater than 100 C
            print("Temp can not be > 100") #if it is, prints error string and ends program
        else:
            fFahrenheit = ((9.0 / 5.0) * fTemp) + 32 #if it isn't over 100 C, calculate for C to F | Fahrenheit = ((9.0 / 5.0) * USER ENTERED TEMP) + 32
            print(f"The Fahrenheit equivalent is: {fFahrenheit:.1f}") #prints C to F conversion, formated to 1 decimal point