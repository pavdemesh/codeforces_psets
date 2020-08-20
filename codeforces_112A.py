string1 = str(input())
string2 = str(input())

if string1.lower() < string2.lower():
    print("-1")
elif string1.lower() > string2.lower():
    print("1")
else:
    print("0")
