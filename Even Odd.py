#Find Even Odd Count in Array 

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

print(arr)   
even_count = 0 
odd_count = 0 

for i in arr :
    if i % 2 == 0 :
        even_count = even_count + 1
    else : 
        odd_count = odd_count + 1
 

print("Even Count:", even_count)        
print("Odd Count:", odd_count)



num = int(input("Enter a no.:"))
if num % 2 == 0 :
    print("Even")
else :
    print("Odd")