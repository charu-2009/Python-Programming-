# Count Words in a Sentence

a = input("Enter sentence: ")

count = 1

for i in range(len(a)):
    if a[i] == " ":
        count +=1

print("Words:", count )