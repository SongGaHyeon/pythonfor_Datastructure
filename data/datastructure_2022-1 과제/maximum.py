def maximum(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c


a, b, c = input().split()  # ex) 1 2 3
a, b, c = int(a), int(b), int(c)

# call the maximum function to find the maximum number among a,b,c
# and, print that maximum


maxi = maximum(a, b, c)
print(maxi)


