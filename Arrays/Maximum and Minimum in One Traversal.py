#Find Largest and Smallest Element in Array 

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

print(arr)   
largest = arr[0]
smallest = arr[0]

for i in arr :

    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest =", largest)
print("Smallest =", smallest)