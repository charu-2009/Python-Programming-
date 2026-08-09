# ==========================================
# DAY 2 - PYTHON BASICS
# ==========================================


# ------------------------------------------------
# 1. Print Numbers from 1 to N
# ------------------------------------------------

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)


# ------------------------------------------------
# 2. Print Even Numbers from 0 to 50
# ------------------------------------------------

for i in range(0, 51, 2):
    print(i)


# ------------------------------------------------
# 3. Sum of Numbers from 1 to N
# ------------------------------------------------

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)


# ------------------------------------------------
# 4. Multiplication Table
# ------------------------------------------------

number = int(input("Enter a number: "))

print(f"\nMultiplication Table of {number}:")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# ------------------------------------------------
# 5. Find Factorial of a Number
# ------------------------------------------------

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print("Factorial =", factorial)


# ------------------------------------------------
# 6. Count Even and Odd Numbers from 1 to N
# ------------------------------------------------

n = int(input("Enter a number: "))

even_count = 0
odd_count = 0

for i in range(1, n + 1):

    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Count:", even_count)
print("Odd Count:", odd_count)


# ------------------------------------------------
# 7. Reverse a Number
# ------------------------------------------------

n = int(input("Enter a number: "))

reversed_num = 0
temp = abs(n)

while temp > 0:

    last_digit = temp % 10
    reversed_num = (reversed_num * 10) + last_digit

    temp //= 10

if n < 0:
    reversed_num = -reversed_num

print("Reversed Number:", reversed_num)


# ------------------------------------------------
# 8. Count Numbers from 1 to N
# ------------------------------------------------

n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    count += 1

print("Count:", count)


# ------------------------------------------------
# 9. Count Number of Digits
# ------------------------------------------------

n = 123456

count = 0
temp = abs(n)

if temp == 0:
    count = 1
else:

    while temp > 0:
        count += 1
        temp //= 10

print("Number of Digits:", count)


# ------------------------------------------------
# 10. Reverse a Number using While Loop
# ------------------------------------------------

n = 12345

reversed_num = 0
temp = abs(n)

while temp > 0:

    last_digit = temp % 10
    reversed_num = (reversed_num * 10) + last_digit

    temp //= 10

print("Reversed Number:", reversed_num)


# ------------------------------------------------
# 11. Sum of Digits
# ------------------------------------------------

n = 12345

digit_sum = 0
temp = abs(n)

while temp > 0:

    last_digit = temp % 10
    digit_sum += last_digit

    temp //= 10

print("Sum of Digits:", digit_sum)


# ------------------------------------------------
# 12. Check Palindrome Number
# ------------------------------------------------

n = 121

original = n
reversed_num = 0
temp = abs(n)

while temp > 0:

    last_digit = temp % 10
    reversed_num = (reversed_num * 10) + last_digit

    temp //= 10


if original == reversed_num:
    print("Output: Palindrome")
else:
    print("Output: Not Palindrome")


# ------------------------------------------------
# 13. Find Largest Digit in a Number
# ------------------------------------------------

n = 58321

largest = 0
temp = abs(n)

while temp > 0:

    last_digit = temp % 10

    if last_digit > largest:
        largest = last_digit

    temp //= 10

print("Largest Digit:", largest)


