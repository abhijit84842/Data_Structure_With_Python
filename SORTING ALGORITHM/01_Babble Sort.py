'''
Algo-> Ascending Order..

step-1 -> Strating with the first element(index=0) and compare the current element with the next element.

step-2 -> if the currenet element is graterthan the next element then swap of them.

step-3 ->  if current element is less than the next element , move to the next element and Repeat STEP-1.

'''



list1=[13,32,26,35,10]
for j in range(len(list1)-1):       # to continue the other iteration
    for i in range(len(list1)-1):            # how many time compare the value  ......"here is 5 elemenet but we compare the value 4 times"
        if list1[i] > list1[i+1]:                   # if the first element is > the next element
            list1[i], list1[i+1]=list1[i+1] , list1[i]            # simply swap the element
print(f"the sorted list is {list1}")