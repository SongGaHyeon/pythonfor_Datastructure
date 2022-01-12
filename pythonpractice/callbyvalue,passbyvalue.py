#제목 두 개는 같은 개념
# 숫자 객체는 변경될 수 없는 immutable
def change(num):
    num=num+10
    print("change내의 num 값:", num)
    print("change내의 num의 주소(id) :", id(num))
    return num

# 파이썬에서는 모든 값들이 객체로 이루어져 있다
n = 100
# id함수는 매개변수 값으로 객체를 받아서 그 객체의 고유한 주소값을 반환해주는 함수

print("호출 전 n의 주소(id):", id(n))
print("호출전 n의 값:", n)
x=change(n)
print("호출 후 x의 주소", id(x))
print("호출 후 x의 값:", x)
print("호출 후 n의 주소", id(n))
print("호출 후 n의 값:", n)




