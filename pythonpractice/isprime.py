# 사용자로부터 정수를 입력받아 소수인지 판별
# True 혹은 False  출력

def is_prime(num):
    for i in range(2,num):
        temp= True
        if num%i==0:
            temp=False
        else:
            temp=True
        return temp
prime=int(input("정수를 입력하세요:"))

print("입력하신",prime,"은 소수인지의 결과가",is_prime(prime))


