import time, random
import numpy as np


def sum(A, n):
    B = []
    B = np.zeros((n, 2))
    for i in range(n):
        for j in range(n):
            B[i][j] += A[i]


# code here

# n = 1 이상 5000 이하 정수 값 입력''
n = int(input())
A = []
# 리스트 A에 랜덤 정수 값 n개 채움
for i in range(n):
    A.append(random.randint(0, 101))
# sum 함수 호출 + 시간 측정
before = time.process_time()
sum(A, n)
after = time.process_time()
print(after - before)

# 함수의 수행시간을 출력