#Find Sum of All Element in Array 

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

print(arr)   
sum = 0 

for i in arr :
    sum = sum + i 
        
print("Toatl Sum:", sum)