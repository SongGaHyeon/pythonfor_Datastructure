# # 재귀함수 형태 (약간 Pseudo code)
# def Fivo(n,r):
#     if(n<=0):
#         return 0
#     elif (n==1):
#         return r[n]=1
#     return r[n]=Fivo[n-1,r]-Fivo[n-2,r]

# 2번씩 트리의 높이 k만큼 반복하는 형태
# 시간 복잡도는 O(2^n)--> 알고리즘의 성능이 좋지 않음


# C로. 재귀호출 없이
# Fivo(n, r)
# {
#     if(n<=0)
#         return 0
#     else if(n==1)
#         return r[n] = 1;
#     else if(r[n]>0) ············ 추가한 부분
#         return r[n]; ··········· 추가한 부분
#     return r[n] = Fivo[n-1, r] - Fivo[n-2,r];
# }

# O(n) 의 시간복잡도


# 그렇다면
# printFivo(n) {
#     for(i=1 to n)
#         print(Fivo(i))
# }
#
# Fivo(n) {
#     if(n<=0)
#         return 0
#     else if(n==1)
#         return 1
#     return Fivo(n-1) + Fivo(n-2)
# }
#
# 이것은 시간복잡도가 O(2^n) 이다
# https://www.youtube.com/watch?v=VcCkPrGaKrs 이거 보기