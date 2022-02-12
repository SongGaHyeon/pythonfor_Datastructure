n = int(input())

#줄 개수 입력받기
a = []

# //리스트에 나열
for i in range(n):
    a.append(int(input()))

# //받을 수만큼 a에 넣기

a.sort()
# //a를 sort이용해서 정렬
for i in range(n):
    print(a[i])