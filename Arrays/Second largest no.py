# Find the Second Largest No. in Array

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)

largest = arr[0]
second = arr[0]

for i in arr:

    if i > largest:
        # What should happen here?
        second = largest 
        largest = i

    elif largest > i > second  :
        # What should happen here?
        second = i 
    
    #else : 
        #print("New Number")

print("Second Largest =", second)