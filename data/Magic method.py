# def add(self, other):
#   return Point(self.x+ other.x, self.y+other.y)
# p= Point(1,2)
# q= Point(3,4)
# r= p.add(q)
# print(r)

# 위와 같이 한다면 더한 값이 출력되지만, r=p+q 형식으로는 사용하지 못한다
# 따라서 이를 해결하기 위해 __add__ 를 사용할 수 있다

# def __add__(self, other):
#   return Point(self.x+ other.x, self.y+other.y)
# r= p+q
# print(r)

#  위의 경우 실제 호출되는 것은
# r= p.__add__(q) 가 출력된다.

#def __rmul__(self, other):
#   return Point(self.x*other, self.y*other)
# 이와 같이 오른쪽에 self가 온다고 할 수 있다
# 이를 이해하기 위한 예시로는

# p= Point(1,2)
# q= Point(3,4)
# r= p-q
# print(r)
# r= 3*p --> 이것은 가능하나
# r=p*3 -->에러가 난다
#  즉, 오른쪽에 Point클래스에 속하는 타입이 들어와야한다.



