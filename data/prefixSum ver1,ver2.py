import time, random


def prefixSum1(X, n):
    S = []
    for i in range(0, n):
        S.append(0)
        for j in range(0, i + 1):
            S[i] += X[j]


# code for prefixSum1

def prefixSum2(X, n):
    # code for prefixSum2
    S = []

    S.append(X[0])
    # 	인덱스로 접근바로 하지못하는 거 주의
    for i in range(1, n):
        S.append(S[i - 1] + X[i])


random.seed()  # random 함수 초기화
# n 입력받음
n = int(input())
X = []
# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
for i in range(0, n):
    X.append(random.randint(-999, 999))
# prefixSum1 호출
before_one = time.process_time()
prefixSum1(X, n)
after_one = time.process_time()
print(after_one - before_one)
# prefixSum2 호출
before_two = time.process_time()
prefixSum2(X, n)
after_two = time.process_time()
# 두 함수의 수행시간 출력
print(after_two - before_two)
