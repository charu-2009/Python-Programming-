# Count Vowels in String

a = input("Enter string: ")
b = a.lower()

count = 0

for i in range(len(b)):
    if b[i] in "aeiou":
        count += 1 

print("Vowels=", count)
 