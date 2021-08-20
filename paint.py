#******************************************************************************
# paint.py
#******************************************************************************
# Name: Anthony Calo
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
rs = float(input("Enter Robbie Red's starting point: "))
re = float(input("Enter Robbie Red's ending point: "))

bs = float(input("Enter Bert Blue's starting point: "))
be = float(input("Enter Bert Blue's ending point: "))
#creating a variable for differences so they can be used in later formula
rd = re - rs
bd = be - bs
overlaprlow = re - bs
overlaprhigh = be - rs
td = rd + bd
#if they dont intercept just the td otherwise totaldistance will == total distance of the two
if re <= bs or be <= rs:
   total_distance = td
   print("The total distance painted is equal to", td)
else:
    total_distance = "different"
#if they intercept and red is lower
if re >= bs and bs > rs and re <= be and total_distance != td:
    print("The total distance pained is equal to ", (td - overlaprlow))
#if they intercept and red is higher
if be > rs and bs < rs and re >= be and re >= bs and total_distance !=td:
    print("the total distance pained is equal to ", (td - overlaprhigh))
#if red engulfs all of blue
if rs <= bs and re >= be:
    print("the total distance pained is equal to ", rd) 
#blue encapsulates red
if rs >= bs and re <= be:
    print("the total distance pained is equal to ", bd) 