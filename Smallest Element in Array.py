#Find Smallest Element in Array 

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

print(arr)   
smallest = arr[0]

for i in arr :

    if (i < smallest):
        smallest = i
        
print("Smallest no:", smallest)