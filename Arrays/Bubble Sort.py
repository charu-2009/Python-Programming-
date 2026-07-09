# Bubble Sort 

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

print(arr) 

for i in range(n - 1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    #elif arr[j] < arr[j+1]:         # Not Needed
        #arr[j] = arr[j+1]         
        #arr[j+1] = arr[j+1+1]
    #else :
        #print("Not found")
print(arr)

