# Linear Search 

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

print(arr) 

key = int(input("Enter the element to search:"))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        found = True
        print("Element at index :", i)
        break
    #else :
        #print("Element Not Found")
if found == False :
    print("Element Not Found")