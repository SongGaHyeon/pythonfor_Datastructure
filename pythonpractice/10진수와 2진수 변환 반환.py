# 10진수를 입력받아 2진수 문자열로 변환 출력
# 함수 decTobin(num)

def decTobin(num):
    binary=""

    while num!=0:
        value=num%2
        if value==0:
            binary+="0"
        else:
            binary+="1"
        num=num//2
        print("num: ",num)
    return binary

decNum=int(input("10진수를 입력하시오:"))
print("10진수 ",decNum,"을 2진수로 변경한 값",decTobin(decNum))

# bin() 2진수로 변환하는 내장함수
# oct() 8진수로 변환하는 내장함수
# hex() 16진수로 변환하는 내장함수

#  2진수를 ->10진수로
# print(int("0b1010",2))
# 8진수를->10진수로
# print(int("0o12",8))
# 16->10도 같은 방식

