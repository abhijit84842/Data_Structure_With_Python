'''
Algo->

Step-1 -> Consider the first element to be sorted and the rest to be unsorted .

Step-2 -> take the first element in the unsorted part(u1) and compare it with sorted part element(s1).

Step-3 -> if u1 < s1 then insert u1 in the correct index, else leave it as it is.

Step-4 -> take next element in the unsorted part and comapre with the sorted elements.

Step-5 -> Repeat 3 and 4 untill all the elements are sorted.

'''

def insertionsort(my_list):
    for index in range(1,len(my_list)):
        current_ele=my_list[index]
        pos=index
        while current_ele < my_list[pos-1] and pos >0:
            my_list[pos]=my_list[pos-1]
            pos=pos-1
        my_list[pos]=current_ele

list1=[10,4,25,1,5]
insertionsort(list1)
print(list1)