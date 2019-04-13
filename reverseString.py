def reverse(string):
    string = "".join(reversed(string))
    return string

s = "StringToReverse"

print ("The origignal string is : ",end="")
print (s)

print ("The reversed string (using reversed) is :", end="")
print (reverse(s))

