# Example 6: Using lists as stacks and queues การใช้ลิสต์เป็นสแตก (Stack) และคิว (Queue)

# Stack operations (Last In, First Out - LIFO) การดำเนินการกับสแตก (LIFO - Last In, First Out)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
popped_item = stack.pop()
print("Popped item from stack:", popped_item) # Output: Popped item from stack: 3 แสดงผล: Popped item from stack: 3

# Queue operations (First In, First Out - FIFO) การดำเนินการกับคิว (FIFO - First In, First Out)
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
dequeued_item = queue.popleft()
print("Dequeued item from queue:", dequeued_item) # Output: Dequeued Item from queue: 1 แสดงผล: Dequeued item from queue: 1