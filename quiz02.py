# 두개 정수 입력받아 두 수 중에 더 큰 수 찾아서 리턴하는 함수

x=int(input("x 입력:"))
y=int(input("y 입력:"))

def morebig(x,y):
    if x>y:
        return x
    else:
        return y
    #temp에 저장해놓고 return temp를 하는 것이 더 효율적임

print(morebig(x,y))


#모듈화를 시킬 때는 python file에 def들을 선언한 뒤,
# 다른 파일에서 파일명.함수명으로 호출 가능하다
# 즉 함수를 모아둔 파일 이름이 calc 일때,
# from calc import * 을 포함시키기!!!!
# 그대로 호출만 하면 가능

