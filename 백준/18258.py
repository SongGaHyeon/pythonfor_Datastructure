from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
stack = deque([])


def push(x):
    stack.append(x)


def pop():
    if not stack:
        return -1
    return stack.popleft()


def size():
    return len(stack)


def empty():
    if not stack:
        return 1
    return 0


def front():
    if not stack:
        return -1
    return stack[0]


def back():
    if not stack:
        return -1
    return stack[-1]


for _ in range(n):
    command = input().split()
    if 'push' in command:
        push(command[1])
    elif 'front' in command:
        print(front())
    elif 'back' in command:
        print(back())
    elif 'size' in command:
        print(size())
    elif 'empty' in command:
        print(empty())
    else:
        print(pop())


        # 코드 이해 중심 ver