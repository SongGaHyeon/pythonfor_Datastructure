# Point 클래스는 2차원을 위한 클래스이기 때문에
#  3,4 여러 차원 벡터를 자유롭게 표현할 수 있도록 하기 위해서는
# Vector 사용 해야함!!

# def function(*args): -->  임의의 개수의 매개변수들을 tuple args 를 통해 전달 가능

def __init__(self, *args):
    self._coords=list(args)
    # 좌표 값을 리스트 _coords에 저장

    # _coords?
    # _하나로 시작하는 멤버 변수는 nonpublic 변수로 다른 곳에서
    # import 해서 사용하는 경우 import되지 않고 감춰진다

def __len__(self):
    return len(self._coords)

def __getitem__(self, k):
    return self._coords[k]

def __setitem__(self, k, val):
    self._coords[k]=val


# __len__과 __getitem__ 메쏘드 정의 시 해당 클래스에
# 대한 iterator가 자동으로 정의
# iterator-> for루프에서 각 원소를 차례대로 접근하는데 사용

# 1. v= Vector(1,2,3)
#  3차원 벡터 v 생성
# 2. print(v)  #(1,2,3)
# for c in v: #for루프를 돌면서 c=v[0], v[1],v[2] 가 된다
#   print(c, end=" ")
# print()
# 1 2 3
