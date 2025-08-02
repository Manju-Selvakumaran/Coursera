istring = input("Enter the string : ")
newstr = ''
for nucleo in istring :
    if nucleo == "A" :
        newstr = newstr+"T"
    elif nucleo == "T" :
        newstr = newstr + "A"
    elif nucleo == "C":
        newstr = newstr + "G"
    elif nucleo == "G":
        newstr = newstr + "C"
rstring = newstr[::-1]
print(rstring)
