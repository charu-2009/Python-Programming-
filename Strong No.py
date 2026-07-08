# Strong No.

a = int(input("Enter number:"))

original = a

sum = 0

while a != 0:

    digit = a % 10

    if digit < 1 :
        print("Factorial not defined.")

    else :
        f = 1 
        for i in range(1, digit+1) : 
            f = f*i

    sum += f

    a = a // 10

if sum == original:

    print("Strong No.")

else:

    print("Not Strong No.")