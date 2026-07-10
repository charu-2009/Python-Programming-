# Count Alphabets, Digits, and Special Characters

a = input("Enter string: ")

alphabets = 0
digits = 0 
specialch = 0

for i in range(len(a)):
    if a[i].isalpha():
        alphabets += 1 
    elif a[i].isdigit():
        digits += 1
    else :
        specialch += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special Characters:", specialch)