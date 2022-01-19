class Node:
    def __init__(self,key=None):
        self.key=key
        self.next=self
        self.prev=self
    def __str__(self):
        return str(self.key)
#값을 key로 저장, (처음엔 None) , 다음 연결고리와 이전 연결고리 선언
# 노드 클래스임
class DoublyLinkedList:
    def __init__(self):
        self.head=Node()
        # head 부분
        self.size=0
    # size부분(0으로 시작)
    #dummy 노드라고 부른다
    def __iter__(self):
        # iterator
        v=self.head
        while(v!=self.head):
            yield v
            # yield ->일종의 반환값(return )
            v=v.next
    def __len__(self):
        return self.size

    def splice(self, a,b,x):
        # 6개의 링크만 변경하기 때문에 상수시간 내에 해결 가능 O(1)
        # 양방향 연결 리스트의 연산은 대부분 splice 이용
        if(a==None or b==None or x==None): return
            # a~b구간을 잘라서 x의 다음 자리에 추가

        ap=a.prev
        bn=b.next

        # 일정 구간 자르기[a,..b]
        ap.next=bn
        bn.prev=ap

        # x 옆에 자른 구간 추가
        xn=x.next
        xn.prev=b
        b.next=xn
        a.prev=x
        x.next=a
        # 이 경우, 연결링크만 변경하면 됌'

        # 조건 1: a 노드 다음에 b 노드가 존재한다. (바로 옆이 아니어도 상관없음)
        #
        # 조건 2: a 노드와 b 노드 사이에 head(더미) 노드가 존재하지 않는다.
        #
        # 조건 3: a 노드와 b 노드 사이에 x 노드가 존재하지 않는다.


    def moveAfter(self, a, x):
        self.splice(a,a,x)
    #     특정 노드 앞으로 이동

    def moveBefore(self, a, x):
        x=x.prev
        self.splice(a,a,x)
        # 특정 노드 뒤로 이동

    def insertAfter(self, x,key):
        self.moveAfter(Node(key),x)

    def insertBefore(self,x,key):
        self.moveBefore(Node(key),x)

    def pushFront(self, key):
        # 맨 앞에 노드 추가
        self.insertAfter(self.head,key)
    def pushBack(self,key):
        # 맨 뒤에 노드 추가
        self.insertBefore(self.head,key)

    def search(self,key):
        v=self.head
        while(v.next!=self.head):
            # head노드로 탐색을 시작해서 돌아올 때까지
            if(v.key==key):
                return v
            # 찾는 노드가 있을 경우 해당 노드 리턴
            v=v.next
        return None
    # 아무리 찾아도 없을경우 None 리턴


    def remove(self,x):
        if(x==None or x==self.head): return
        # 삭제 과정은 탐색 연산도 필요
        # 따라서 모든 노드를 검색해야하므로
        # O(n) 시간 내에 가능
        xp=x.prev
        xn=x.next

        xp.next= x.next
        xn.prev= x.prev
        del x