# Binary Search 

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

print(arr) 

key = int(input("Enter the element to search:"))

low = 0
high = len(arr) - 1

found = False 

while low <= high:

    mid = (low + high) // 2
    
    if arr[mid] == key :
        print("Element found at index", mid)
        found = True
        break 

    elif key < arr[mid] :
        high = mid - 1 

    elif key > arr[mid] :
        low = mid + 1 
       
if found == False :
    print("Element Not Found")




# Binary Search 

n= int(input("Enter elements:"))

arr=[]

for k in range(n):
    
    a = int(input("Enter the element:"))
    arr.append(a)

print(arr) 

key = int(input("Enter the element to search:"))

low = 0
high = len(arr) - 1

found = False 

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key :
        print("Element found at index", mid)
        found = True
        break 
    elif key < arr[mid] :
        #low = 0
        high = mid - 1 
        #mid = (low + high) // 2
        #if arr[mid] == key :
            #print("Element found at index", mid)
    elif key > arr[mid] :
        low = mid + 1 
        #high = len(arr) - 1
        #mid = (low + high) // 2
        #if arr[mid] == key :
            #print("Element found at index", mid)
    #else :
        #print("Element Not Found")
if found == False :
    print("Element Not Found")

