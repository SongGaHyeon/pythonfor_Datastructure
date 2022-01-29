from sys import stdin
input = stdin.readline
set1 = set()
set2 = set()

N, M = map(int, input().split())
for i in range(N):
    set1.add(input().strip("\n"))
for j in range(M):
    set2.add(input().strip("\n"))

ans = sorted(list(set1.intersection(set2)))
print(len(ans))
for os in ans:
    print(os)