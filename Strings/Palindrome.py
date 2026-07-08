# Check for Palindrome

a = input("Enter string: ")
b = a.lower()

palindrome = True

for i in range(len(b) // 2):
    if b[i] != b[-i - 1]:
        palindrome = False
        break

if palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")