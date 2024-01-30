# We use 2 modules in this program..
'''
1) collection.deque()           
2) queue.LifoQueue()
'''

# Collection Modules..
import collections

stack=collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

#print(type(stack))          # deque class..

stack.pop()     # to remove the item from stack..
print(stack)

# Check stack is empty or not..
print(not stack)            # It returns True or False..




# Queue modules

'''
We use in queue modules put() and get() instead of append() and pop() method....

'''

import queue
stack=queue.LifoQueue()
stack.put(10)       # we use put() instead of append() to add data in stack..
stack.put(20)           
stack.put(30)

print(stack.queue)

stack.get()      # we use get() instead of pop() to remove data from stack..

print(stack.queue)
