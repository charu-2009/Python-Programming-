# Fibonanci Series 

a = int(input("Enter a no.:"))
first = 0
second = 1
for i in range(a):
    #print(first)
    next_num = first + second 
    first = second
    second = next_num
print(first)
#print(second)
#print(next)
