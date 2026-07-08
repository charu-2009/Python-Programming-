# Reverse a String

a = input("Enter string: ")
b = a.lower()

reverse = ""

for i in range(len(b)):
    reverse += b[-i-1]

print(reverse)
