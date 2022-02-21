def solution(d, budget):
    d.sort()
    i=0
    while i < len(d):
        if budget >= d[i]:
            budget-=d[i]
            i+=1
        else:
            break
    return i