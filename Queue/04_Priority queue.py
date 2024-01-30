'''
Priority Queue is an extension of queue with following properties.

1) Every item has a priority associated with it.
2) An element with high priority is dequeued before an element with low priority.
3) If two elements have the same priority, they are served according to their order in the queue.
'''
# lowest element -> highest priority
# highiest element -> lowest priority

# prority impementation using 1) list  
                            # 2) PriorityQueue()   CLASS

'''Implementation using List'''
q=[]
q.append(2)
q.append(3)
q.append(1)
q.append(4)

q.sort()
print(q)                #output=> [1, 2, 3, 4]


# To remove the element..
q.pop(0)
q.pop(0)
print(q)            #output=> [3, 4]


'''Implenetation using MOdules'''
import queue
q1=queue.PriorityQueue()
q1.put(10)
q1.put(20)
q1.put(30)
q1.put(40)
q1.put(50)
print(q1.queue)                    #output=>  [10, 20, 30, 40, 50]


# TO remove ..
q1.get()
print(q1.queue)                 #output=>   [20, 40, 30, 50]