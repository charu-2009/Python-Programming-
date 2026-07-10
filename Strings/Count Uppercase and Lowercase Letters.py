# Count Uppercase and Lowercase Letters

a = input("Enter string: ")

uppercase = 0
lowercase = 0 

for i in range(len(a)):
    if a[i].islower():
        lowercase += 1 
    elif a[i].isupper():
        uppercase += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)