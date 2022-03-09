a, b, v = map(int, input().split())
n = 0
if (v - b) % (a - b) != 0:
    n = ((v - b) // (a - b)) + 1
else:
    n = ((v - b) // (a - b))
print(n)