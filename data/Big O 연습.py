# 다음 알고리즘이 n^2logn 걸리는 이유 살펴보기

# algorithm doSomething(n):
#     count=0
#     for i=0 to n-1 do          #n시간
#         for j=0 to n-1 do      #n시간
#             k=1

            # while k<n do       #count와 k의 관계 주목
            #     count+=1
            #     k=k*2          #k=2^count-1
        # return count   #따라서 count=n^logn 의 big o가 걸린다다    # end_of_algorithm

