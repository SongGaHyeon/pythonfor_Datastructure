class Queue:
    def __init__(self):
        self.items=[]
        self.front_index=0 #다음 dequeue 될 값의 인덱스 기억

    def enqueue(self,val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index==len(self.items):
            print("Queue is empty")
            return None
        else:
            x=self.items[self.front_index]
            self.front_index+=1
            # 해결안된 부분: 근데 삭제는 안해주는 것인가??
            return x