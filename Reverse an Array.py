# Reverse an Array

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

print(arr)

reverse = []

for i in range(len(arr)):
    reverse.append(arr[-i-1])

print(reverse)