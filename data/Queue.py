class Queue:
    def __init__(self):
        self.items=[]
        self.front_index=0 #다음 dequeue 될 값의 인덱스 기억

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index==len(self.items): #큐가 비어있을 때
            print("Queue is empty")
            return None
        else:
            x=self.items[self.front_index]
            self.front_index+=1
            # 해결안된 부분: 근데 삭제는 안해주는 것인가??
            # 아!! 삭제가 아예 front_index를 옮겨주는 거라고 할 수 있다!!
            return x

    def isEmpty(self):
        if(self.front_index==len(self.items)):
            print("Queue is empty")
        else:
            return len(self.items)-self.front_index
        # 큐가 비어있으면 문구 출력, 아니면 길이 return

    def front(self): #가장 왼쪽 저장된 값을 삭제하지 않고 리턴
        return self.items[self.front_index]

    def len(self):
        return len(self.items)-self.front_index


    #여기서 시간복잡도는 O(1)