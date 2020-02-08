name = input("Enter  a name: ")
output =""

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)
some_list = []
for r in (("ka"),("tu"),( "mi"),("te"),("ku"),("lu"),("ji"),("ri"),("ki"),("zu"),("me"),("ta"),("rin"),("to"),("mo"),("no"),("ke"),("shi"),("ari"),("chi"),("do"),("ru"),("mei"),("na"),("fu"),("zi"),(" ")):
    some_list.append(list(find_all(name, r)))
some_set = []
for i in some_list:
    for j in i:
        some_set.append(j)
some_set = list(set(some_set))


index = 0
string_array = []
too_short = False
while index < len(some_set)-1:
    if too_short == True:
        start = some_set[index-1]
        end = some_set[index+1]
        too_short = False
    else:
        start = some_set[index]
        end = some_set[index+1]
    if end-start < 2:
        if name[start:end] == " ":
             string_array.append(name[start:end])
        else:
            too_short = True
    else:    
        string_array.append(name[start:end])

    index = index + 1
string_array.append(name[some_set[index]:len(name)])
output = ""
for i in string_array:
    for r in (("ka", "a"),("tu","b"),( "mi", "c"),("te","d"),("ku", "e"), ("lu","f"),("ji","g"),("ri","h"),("ki","i"),("zu","j"),("me","k"),("ta","l"),("rin","m"),("to","n"),("mo","o"),("no","p"),("ke","q"),("shi","r"),("ari","s"),("chi","t"),("do","u"),("ru","v"),("mei","w"),("na","x"),("fu","y"),("zi","z"),(" "," ")):
        if i == r[0]:
            output = output + i.replace(*r)
print (output)