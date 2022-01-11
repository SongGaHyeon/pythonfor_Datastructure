

def increment_one(a):
    return a+1
# 이것은 시간이 O(1)

def number_of_bits(n):
    count=0
    while n>0:
        n=n//2
        count+=1
    return count
# O(log2n) 시간이 걸리는 알고리즘

# algorithm array_sum(A,B,n):
#     sum=0
#     for i=0 to n-1 do
#     for j=0 to n-1 do
#       sum+=A[i]*B[j]
# return sum
# O(n^2) 시간이 걸리는 알고리즘


#algorithm mult_matrices(A,B,n)
#   input: n*n의 2차열 행렬 A,B
#   output: C=AxB

#   for i=1 to n do
#       for j= to n do
#           C[i][j]=0
#   for i=1 to n do
#       for j=1 to n do
#           for k=1 to n do
#               C[i][j]+=A[i][k]*B[k][j]
#   return C
# O(n^3) 시간 알고리즘


#O(2^n) 이상의 시간이 필요한 알고리즘
        # def fibonacci(k):
        #   if k<=1: return k
        #   return fibonacci(k-1)+fibonacci(k-2)
