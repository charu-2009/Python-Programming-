# ==========================================
# DAY 3 - PYTHON BASICS
# ==========================================


# ==========================================
# 1. Print All Elements of an Array
# ==========================================

numbers = [10, 20, 30, 40, 50]

for i in numbers:
    print(i)


# ==========================================
# 2. Find Sum of All Elements in Array
# ==========================================

n = int(input("Enter number of elements: "))

arr = []

for k in range(n):
    a = int(input("Enter the element: "))
    arr.append(a)

print("Array:", arr)

total_sum = 0

for i in arr:
    total_sum = total_sum + i

print("Total Sum:", total_sum)


# ==========================================
# 3. Find Largest Number in Array
# ==========================================

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print("Largest Number:", largest)


# ==========================================
# 4. Find Smallest Number in Array
# ==========================================

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print("Smallest Number:", smallest)


# ==========================================
# 5. Count Even and Odd Numbers
# ==========================================

even_count = 0
odd_count = 0

for i in arr:
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even Count:", even_count)
print("Odd Count:", odd_count)


# ==========================================
# 6. Reverse an Array
# ==========================================

reverse = []

for i in range(len(arr)):
    reverse.append(arr[-i - 1])

print("Reversed Array:", reverse)


# ==========================================
# 7. Find Second Largest Number
# ==========================================

largest = arr[0]
second = arr[0]

for i in arr:

    if i > largest:
        second = largest
        largest = i

    elif largest > i > second:
        second = i

print("Second Largest:", second)


# ==========================================
# 8. Find Duplicate Elements
# ==========================================

unique_items = []
duplicates = []

for num in arr:

    if num not in unique_items:
        unique_items.append(num)

    else:
        if num not in duplicates:
            duplicates.append(num)

print("Duplicate Elements:", duplicates)


# ==========================================
# 9. Linear Search
# ==========================================

key = int(input("Enter the element to search: "))

found = False

for i in range(len(arr)):

    if arr[i] == key:
        found = True
        print("Element found at index:", i)
        break

if found == False:
    print("Element Not Found")


# ==========================================
# 10. Left Rotate an Array
# ==========================================

left_arr = arr.copy()

temp = left_arr[0]

for i in range(len(left_arr) - 1):
    left_arr[i] = left_arr[i + 1]

left_arr[-1] = temp

print("Left Rotated Array:", left_arr)


# ==========================================
# 11. Right Rotate an Array
# ==========================================

right_arr = arr.copy()

temp = right_arr[-1]

for i in range(len(right_arr) - 1, 0, -1):
    right_arr[i] = right_arr[i - 1]

right_arr[0] = temp

print("Right Rotated Array:", right_arr)


# ==========================================
# 12. Check if Two Lists are Equal
# ==========================================

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

are_equal = True

if len(list1) != len(list2):
    are_equal = False

else:
    for i in range(len(list1)):

        if list1[i] != list2[i]:
            are_equal = False
            break

if are_equal:
    print("Lists are Equal")

else:
    print("Lists are Not Equal")


# ==========================================
# 13. Frequency Count
# ==========================================

frequency = []

for i in arr:

    if i not in frequency:
        frequency.append(i)

for i in frequency:

    count = 0

    for j in arr:

        if j == i:
            count += 1

    print(i, "->", count, "times")


# ==========================================
# 14. Removing Duplicate Elements from Array
# ==========================================

unique_items = []

for num in arr:

    if num not in unique_items:
        unique_items.append(num)

print("Array Without Duplicates:", unique_items)


# ==========================================
# 15. Find Common Elements in Two Arrays
# ==========================================

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = []

for element in a:

    if element in b:
        common.append(element)

print("Common Elements:", common)


# ==========================================
# 16. Count Vowels in String
# ==========================================

text = input("Enter string: ")

text = text.lower()

count = 0

for i in range(len(text)):

    if text[i] in "aeiou":
        count += 1

print("Vowels:", count)


# ==========================================
# 17. Count Alphabets, Digits,
#     and Special Characters
# ==========================================

text = input("Enter string: ")

alphabets = 0
digits = 0
special_characters = 0

for i in range(len(text)):

    if text[i].isalpha():
        alphabets += 1

    elif text[i].isdigit():
        digits += 1

    else:
        special_characters += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special Characters:", special_characters)


# ==========================================
# 18. Count Uppercase, Lowercase,
#     Digits, and Special Characters
# ==========================================

text = input("Enter string: ")

uppercase = 0
lowercase = 0
digits = 0
special_characters = 0

for i in range(len(text)):

    if text[i].isupper():
        uppercase += 1

    elif text[i].islower():
        lowercase += 1

    elif text[i].isdigit():
        digits += 1

    else:
        special_characters += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digits)
print("Special Characters:", special_characters)

