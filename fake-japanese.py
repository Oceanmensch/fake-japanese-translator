name = input("Enter  a name: ")
name_list = list(name)
output = "" 
for i in name_list:
    if i == "A" or i == "a": 
        output = output + "ka"
    if i == "B" or i == "b": 
        output = output + "tu"
    if i == "C" or i == "c": 
        output = output + "mi"
    if i == "D" or i == "d": 
        output = output + "te"
    if i == "E" or i == "e": 
        output = output + "ku"
    if i == "F" or i == "f": 
        output = output + "lu"
    if i == "G" or i == "g": 
        output = output + "ji"
    if i == "H" or i == "h": 
        output = output + "ri"
    if i == "I" or i == "i": 
        output = output + "ki"
    if i == "J" or i == "j": 
        output = output + "zu"
    if i == "K" or i == "k": 
        output = output + "me"
    if i == "L" or i == "l": 
        output = output + "ta"
    if i == "M" or i == "m": 
        output = output + "rin"
    if i == "N" or i == "n": 
        output = output + "to"
    if i == "O" or i == "o": 
        output = output + "mo"
    if i == "P" or i == "p": 
        output = output + "no"
    if i == "Q" or i == "q": 
        output = output + "ke"
    if i == "R" or i == "r": 
        output = output + "shi"
    if i == "S" or i == "s": 
        output = output + "ari"
    if i == "T" or i == "t": 
        output = output + "chi"
    if i == "U" or i == "u": 
        output = output + "do"
    if i == "V" or i == "v": 
        output = output + "ru"
    if i == "W" or i == "w": 
        output = output + "mei"
    if i == "X" or i == "x": 
        output = output + "na"
    if i == "Y" or i == "y": 
        output = output + "fu"
    if i == "Z" or i == "z": 
        output = output + "zi"
    if i == " ":
        output = output + " "        
print (output)