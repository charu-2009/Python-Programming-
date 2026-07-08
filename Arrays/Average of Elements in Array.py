#Find Average of Element in Array 

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

print(arr)   
total = 0 

for i in arr :
    total = total + i 

avg = total/n
        
print("Average:", avg)