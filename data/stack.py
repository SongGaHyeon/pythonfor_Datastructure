class Stack:
    def __init__(self):
        self.items=[]

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self): #len()로 호출하면 stack의 item 수 반환
        return len(self.items)

    def isEmpty(self):
        return len(self)==0