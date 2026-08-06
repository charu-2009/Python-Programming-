# Check if Two Lists are Equal

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

are_equal = True

if len(list1) != len(list2):
    are_equal = False

else:
    for i in range(len(list1)):
        
        if list1[i] != list2[i]:
            are_equal = False
            break


if are_equal:
    print("Lists are Equal")
else:
    print("Lists are Not Equal")