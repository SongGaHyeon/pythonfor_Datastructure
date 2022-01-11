def printInfo(name, age):
    print("==================")
    print("이름:",name)
    print("나이:",age)
    print("=============")
    # return 값이 존재하지않는다면 return 뒤 아무것도 안써도 괜찮음
    return

end_Input="y"
print("이름과 나이를 입력(입력종료 q):")
while True:
    if end_Input=="q":
        print("입력을 종료합니다")
        break
    elif end_Input=="y":
        name=input("회원명을 입력해주세요:")
        age= int(input("회원님의 나이를 입력:"))
        printInfo(name, age)

    end_Input=input("계속 입력하시겠습니까?(y or q):")