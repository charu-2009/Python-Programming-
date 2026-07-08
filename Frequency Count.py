# Frequency Count 

# Removing Duplicate Elements from Array 
# Start

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

unique_items = []

for num in arr:          
    if num not in unique_items:
        unique_items.append(num)

# End

for i in unique_items:
    count = 0 
    for j in arr:
        if j ==i:
            count += 1

    print(i,"->",count,"times")
    