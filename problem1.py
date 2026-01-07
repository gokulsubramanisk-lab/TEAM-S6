from collections import deque
queue = deque()
token = 0
MAX_SIZE = 100
while True:
    command = input().strip().upper()
    if command == "ADD":
        if len(queue) < MAX_SIZE:
            token += 1
            queue.append(token)
            print(f"Token Generated: {token}")
        else:
            print("Queue Full")
    elif command == "SERVE":
        if queue:
            served = queue.popleft()
            print(f"Serving Token: {served}")
        else:
            print("No Students in Queue")
    elif command == "STATUS":
        print(f"Students Waiting: {len(queue)}")
    elif command == "EXIT":
        break
    else:
        print("Invalid Command")
