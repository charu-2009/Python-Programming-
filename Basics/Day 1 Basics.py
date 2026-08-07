# ==========================================
# DAY 1 - PYTHON BASICS
# ==========================================

# Hello World

print("Hello, World!")
print("My name is Charu Jain.")

# Taking User Input

age = int(input("Enter your age: "))
print("Your age is:", age)


# ==========================================
# BASIC OPERATIONS
# ==========================================

# Addition

a = 10
b = 20
print("Sum:", a + b)

# Swapping Two Numbers

a, b = b, a
print("After Swapping:", a, b)


# ==========================================
# FUNCTIONS
# ==========================================

# Area of Rectangle

def area(length, breadth):
    result = length * breadth
    print("Area:", result)

area(30, 50)


# Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Kilometers to Miles

def kilometers_to_miles(km):
    return km * 0.621371


# Simple Interest

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


# BMI Calculator

def bmi(weight, height):
    return weight / (height ** 2)


print("Temperature:", celsius_to_fahrenheit(25))
print("Miles:", kilometers_to_miles(10))
print("Simple Interest:", simple_interest(1000, 5, 2))
print("BMI:", bmi(70, 1.75))


# ==========================================
# ARITHMETIC OPERATIONS
# ==========================================

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)


# ==========================================
# LARGEST OF THREE NUMBERS
# ==========================================

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 >= n2 and n1 >= n3:
    print("Largest:", n1)
elif n2 >= n1 and n2 >= n3:
    print("Largest:", n2)
else:
    print("Largest:", n3)


# ==========================================
# LARGEST NUMBER + EVEN/ODD
# ==========================================

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest Number:", largest)

if largest % 2 == 0:
    print(f"{largest} is Even.")
else:
    print(f"{largest} is Odd.")


# ==========================================
# LEAP YEAR
# ==========================================

year = int(input("Enter a year: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap:
    print("Leap Year")
else:
    print("Not a Leap Year")


# ==========================================
# TERNARY OPERATOR PROGRAMS
# ==========================================

# Voting Eligibility

age = 20
print("Eligible to vote" if age >= 18 else "Not eligible to vote")


# Student Grade

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)


# Positive, Negative or Zero

num = -5

status = (
    "Positive"
    if num > 0
    else ("Negative" if num < 0 else "Zero")
)

print(status)


# Divisible by 5 and 11

num = 55

print(
    "Divisible by both"
    if num % 5 == 0 and num % 11 == 0
    else "Not divisible"
)


# Smallest of Three Numbers

a = 12
b = 5
c = 8

print("Smallest:", min(a, b, c))


# Vowel or Consonant

char = "e"

print(
    "Vowel"
    if char.lower() in "aeiou"
    else "Consonant"
)



