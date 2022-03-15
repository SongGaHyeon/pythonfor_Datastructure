def dot_product(a, b):
    listforab = []
    # allsum=0
    # littlesum=0
    # for i in range(len(a)):
    # 	littlesum+=a[i]*b[i]
    # 	allsum+=littlesum
    # 	littlesum=0
    # return allsum
    # -----------------------------code#1 using one for loop and using two 변수
    for i in range(len(a)):
        listforab.append(a[i] * b[i])
        sum = 0
    for j in range(len(a)):
        sum += int(listforab[j])
    return sum
# ----------------------------code#2
# using list(1D arraylist)


# write the dot_product function here

a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
dot= dot_product(a,b)
print(dot)