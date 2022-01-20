n = int(input())
z = []
for i in range(n):
    num = int(input())
    if num == 0:
        z.pop()
    else:
        z.append(num)
print(sum(z))

#n = int(input())
# z = []
# for i in range(n):
#     num = int(input())
#     if num == 0:
#         z.pop()
#     else:
#         z.append(num)
# print(sum(z))
# 이것도 가능