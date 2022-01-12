def change(string):
    string+="공부합니다"
    print("change 내의 string 값:",string," 주소:",id(string))
    return string

msg="안녕하세요 저는 파이썬을"
print("호출 전 msg값:"+msg)
print("호출 전 msg주소:",id(msg))
change(msg)
print("호출 후 msg값:"+msg)
print("호출 후 msg주소:",id(msg))
msg=change(msg)
print(msg)
print("my작업 후 msg주소:",id(msg))
x=change(msg)
print(x)
print("x주소:",id(x))