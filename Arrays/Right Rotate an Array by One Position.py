# Right Rotate an Array by One Position

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

print(arr) 

temp = arr[-1]

for i in range(len(arr)-1,0,-1):
    arr[i] = arr[i - 1]

arr[0] = temp

print(arr)