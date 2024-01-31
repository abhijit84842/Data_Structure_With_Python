# SELECTION SORT

'''
Step-1 -> Search the list and find out the minimum value

Step-2 -> Swap the smallest number to 0th index.

Step-3 -> take the sublist(Except sorted part) and repeat Step-1 and Step-2 untill list is completely sorted
'''

list1=[56,3,2,78,6,1]
for i in range(len(list1)):
    min_val=min(list1[i:])
    min_index=list1.index(min_val)
    list1[i] , list1[min_index] = list1[min_index],list1[i]


print(list1)
