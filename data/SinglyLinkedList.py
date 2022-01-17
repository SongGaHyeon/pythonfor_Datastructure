from Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
        #첫 노드의 요소와 사이즈 첫 노드를 가르키는 노드라 볼 수 있음

    def __iter__(self):
        #제너레이터
        v=self.head
        while(v!=None):
            yield v
            v= v.next
    def __str__(self):
        return " -> ".join(str(v) for v in self)
    def __len__(self):
        return self.size
    # ---------------------------------------------
    def pushFront(self,key,value=None):
        new_node=Node(key,value) #새로운 노드를 만든다
        new_node.next=self.head #새로운 노드가 기존의 노드를 가리킨다
        self.head=new_node
        self.size+=1
    def pushBack(self,key, value=None):
        new_node=Node(key,value)
        if(self.size==0):
            self.head=new_node
        else:
            tail = self.head
            while(tail.next!=None):
                tail= tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):
        if(self.size==0):
            return None
        else:
            x= self.head
            key= x.key
            self.head =x.next
            self.size-=1
            del x
            return key
    def popBack(self,key):
        #기존 노드를 제거하는 메소드
        if(len(self)==0):
            return None
        else: #안에 하나라도 있다면
            prev,tail=None, self.head
            while(tail.next != None):
                prev=tail
                tail=tail.next
            if(len(self)==1): #len이 있어서 가능
                self.head=None#만약 하나있다면
            else:
                prev.next=tail.next
        key=tail.key
        del tail
        self.size-=1
        return key

    def search(self,key):
        v= self.head
        while(v!=None):
            if (v.key==key):
                return key
            v=v.next
        return None