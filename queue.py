from collections import deque

#deque allows you to easily implement a basic kind of queue, the maxlen 
#set to 4 means its going to store the last 4 items pass in
queue = deque(maxlen=4)


for i in range(1,6):
    queue.append(i) 
    print(queue)
# RESULT:
# deque([1], maxlen=4)
# deque([1, 2], maxlen=4)
# deque([1, 2, 3], maxlen=4)
# deque([1, 2, 3, 4], maxlen=4)
# deque([2, 3, 4, 5], maxlen=4)

# you can append to the leftside(item at index 0 in list) of the queue
queue.appendleft(6)
print(queue)
#RESULT:
#deque([6, 2, 3, 4], maxlen=4)

# pop removes the last item from the queue and also returns it like so:
popped_item = queue.pop()
print(popped_item)
# RESULT:
# 4

# you can also popleft to remove an item at the leftside of the queue
popped_item=  queue.popleft()
print(popped_item)
# RESULT:
# 6