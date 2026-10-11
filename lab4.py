# Implement Stack using Python

stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push operations:")
print(stack)

# Pop element
element = stack.pop()

print("Popped element:", element)
print("Stack after pop operation:")
print(stack)

# Peek operation
if len(stack) > 0:
    print("Top element:", stack[-1])
else:
    print("Stack is empty")

# Check if stack is empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")
    print("-------Implementing Queue operation--------")

    # Implement Queue using Python

queue = []

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue operations:")
print(queue)

# Dequeue element
element = queue.pop(0)

print("Dequeued element:", element)
print("Queue after dequeue operation:")
print(queue)

# Peek operation
if len(queue) > 0:
    print("Front element:", queue[0])
else:
    print("Queue is empty")

# Check if queue is empty
if len(queue) == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")
    print("---------Implementing Binary search using Python-----------")


    # Implement Binary Search using Python

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif target < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1


# Sorted array
arr = [6, 12, 17,23,38,45,77,84,90]

target = 45

result = binary_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")