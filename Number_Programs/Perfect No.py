# Perfect No. 

a = int(input("Enter number:"))

original = a

sum = 0

for i in range(1,a):

    if a % i == 0:
        sum += i
    
#print(sum)


if sum == original:

    print("Perfect No.")

else:

    print("Not Perfect No.")