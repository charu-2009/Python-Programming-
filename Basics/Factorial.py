# Find Factorial of a Number

n = int(input("Enter a no.:"))
if n < 1 :
    print("Factorial not defined.")
else : 
    f = 1 
    for i in range(1, n+1) : 
        f = f*i
    #print(f)
print("Factorial =", f)

