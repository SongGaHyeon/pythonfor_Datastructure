num = int( input())
han = 0

for n in range( 1, num+1 ):
    if n<=99:
        han += 1
    else:
        nums = list(map(int, str(n)))
        if nums[0] + nums[2] == 2* nums[1]:
            han +=1
print(han)
