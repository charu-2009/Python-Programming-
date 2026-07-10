# Find Duplicate Elements in a List

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

unique_items = []
duplicate = []

for num in arr:          
    if num not in unique_items:
        unique_items.append(num)
    else :
        duplicate.append(num)

print(duplicate)