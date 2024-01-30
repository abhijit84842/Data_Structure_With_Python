
# TO add the element in queue..

        # appendleft and pop method


import collections

queue=collections.deque()
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
queue.appendleft(40)
print(queue)

#output=> deque([40, 30, 20, 10])

queue.pop()
queue.pop()
print(queue)       #output=>   deque([40, 30])




# append and popleft method..
import collections
queue1=collections.deque()

queue1.append(10)
queue1.append(20)
queue1.append(30)
queue1.append(40)
queue1.append(50)
print(queue1)         #output=>       deque([10, 20, 30, 40, 50])


# remove the element from the queue..
queue1.popleft()
print(queue1)                  #output=>      deque([20, 30, 40, 50])



# queue Module..

# queue -> Queue()

'''
We use in queue modules put() and get() instead of append() and pop() method....

'''

import queue
q=queue.Queue()

q.put(100)
q.put(200)
q.put(300)
q.put(400)
print(q.queue)      #output=> deque([100, 200, 300, 400])


# To remove the element from queue..
q.get()
print(q.queue)           #output=>        deque([200, 300, 400])