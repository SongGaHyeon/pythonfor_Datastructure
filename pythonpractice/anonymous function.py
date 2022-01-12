def main():
    print("두 정수의 합: ",get_sum(10,50))
    print("두 정수의 합: ",get_sum(100,50))
    print("lamda 이용 두 정수의 합: ", sum(10, 50))
    print("lamda 이용 두 정수의 합: ", sum(100, 50))

def get_sum(x,y):
    return x+y


# lamba키워드를 이용한 sum() 만들기
sum= lambda x,y: x+y
# lambda에서는 변수값을 지정해줄 수 없다
# (lambda x,y:x+y)(10,50) 이렇게는 가능
# lambda 식으로 구성되어진 리스트 데이터
li=[lambda x: x**2, lambda x: x**3, lambda x:x**4]
main()

for f in li:
    print(f(10))