def reverse(string):
    string = "".join(reversed(string))
    return string

s = "StringToReverse"

print ("The origignal string is : ",end="")
print (s)

print ("The reversed string (using reversed) is :", end="")
print (reverse(s))


print ("##########################################")
# Using loop

def reverseloop(s):
    str = ""
    for i in s:
        str = i+ str
    return str

s = "string reverse using loop"

print ("The origianl string is : ",end="")
print (s)

print ("The reversed string using loops is :",end ="")
print (reverse(s))


print ("##########################################")

