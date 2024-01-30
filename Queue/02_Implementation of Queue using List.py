'''
enqueue=append()
dequeue=pop()

# We need to use index with append and pop method because queue follow the FIFO rules..

'''

queue=[]

# to add the elements

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

# remove the element from queue..
queue.pop(0)         # Need to use index number to remove the element becuse queue follow the FIFO AND LILO.
queue.pop(0)
print(queue)



queue1=[]
# Using Insert method
queue1.insert(0,10)
queue1.insert(0,20)
queue1.insert(0,30)
queue1.insert(0,40)
print(queue1)


 # Queue implementation using list..

queue=[]

def add_element():
     element=input("Enter the element..")
     queue.append(element)
     print(queue)

def remove_element():
    if not queue:
        print("Queue is empty..")
    else:
        pop_element=queue.pop(0)

        print(queue)

while True:
    print("Chose the operation number...1=append,2=pop,3=quit..")

    choice=int(input("Plz Choise the number.."))

    if choice==1:
        add_element()
    elif choice==2:
        remove_element()
    elif choice==3:
        break
    else:
        print("Plz enter the correct operation..")
        