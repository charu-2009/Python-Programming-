# Armstrong No. 

a = int(input("Enter number:"))

original = a

sum = 0

while a != 0:

    digit = a % 10

    sum += digit**3

    a = a // 10

if sum == original:

    print("Armstrong")

else:

    print("Not Armstrong")