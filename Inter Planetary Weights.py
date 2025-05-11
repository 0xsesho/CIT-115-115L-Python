#Author: Ethan Boucher
#Class: Py (CIT-115-D02)
#Date: 2/18/2025
#Assignmemt: Inter Planetary Weights


#Named Constants
fMER_FACTOR = .38 #Mercury Gravity factor
fVEN_FACTOR = .91 #Venus Gravity Factor
fEARTH_FACTOR = 1.0 #Earth Gravity Factor
fMOON_FACTOR = .165 #Moon Gravity Factor
fMARS_FACTOR = .38 #Mars Gravity Factor
fJUP_FACTOR = 2.34 #Jupiter Gravity Factor
fSAT_FACTOR = .93 #Saturn Gravity Factor
fURA_FACTOR = .92 #Uranus Gravity Factor
fNEP_FACTOR = 1.12 #Neptune Gravity Factor
fPLUTO_FACTOR = .066 #Pluto Gravity Factor

#Input
sName = input("What is your name?: ") #takes the user's name string and assigns it to the sName variable
fEarthWeight = float(input("How much do you weigh on Earth?: ")) #takes user input weight, converts it to a float and assigns the float to fEarthWeight 

#Calculations
fMerWeight = fEarthWeight * fMER_FACTOR #calculates weight on Mercury
fVenWeight = fEarthWeight * fVEN_FACTOR #calculates weight on Venus
fMoonWeight = fEarthWeight * fMOON_FACTOR #calculates weight on Moon
fMarsWeight = fEarthWeight * fMARS_FACTOR #calculates weight on Mars
fJupWeight = fEarthWeight * fJUP_FACTOR #calculates weight on Jupiter
fSatWeight = fEarthWeight * fSAT_FACTOR #calculates weight on Saturn
fUraWeight = fEarthWeight * fURA_FACTOR #calculates weight on Uranus
fNepWeight = fEarthWeight * fNEP_FACTOR #calculates weight on Neptune
fPlutoWeight = fEarthWeight * fPLUTO_FACTOR #calculates weight on Pluto

#Output
print(f"\n{sName}, here are your weights on our Solar System's planets:") #prints the fstring, assigned sName variable is printed on a new line followed by the string
print(f"Weight on Mercury:{fMerWeight:11.2f}") #prints a fstring, variable fMerWeight is printed as a floating point number with 2 decimals
print(f"Weight on Venus:{fVenWeight:13.2f}") #prints a fstring, variable fVenWeight is printed as a floating point number with 2 decimals
print(f"Weight on our Moon:{fMoonWeight:10.2f}") #prints a fstring, variable fMoonWeight is printed as a floating point number with 2 decimals
print(f"Weight on Mars:{fMarsWeight:14.2f}") #prints a fstring, variable fMarsWeight is printed as a floating point number with 2 decimals
print(f"Weight on Jupiter:{fJupWeight:11.2f}") #prints a fstring, variable fJupWeight is printed as a floating point number with 2 decimals
print(f"Weight on Saturn:{fSatWeight:12.2f}") #prints a fstring, variable fSatWeight is printed as a floating point number with 2 decimals
print(f"Weight on Uranus:{fUraWeight:12.2f}") #prints a fstring, variable fUraWeight is printed as a floating point number with 2 decimals
print(f"Weight on Neptune:{fNepWeight:11.2f}") #prints a fstring, variable fNepWeight is printed as a floating point number with 2 decimals
print(f"Weight on Pluto:{fPlutoWeight:13.2f}") #prints a fstring, variable fPlutoWeight is printed as a floating point number with 2 decimals






