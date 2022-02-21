def cal(taget, left_l2, right_l2, hand):
    if taget == 0:
        taget = 11
    if left_l2 == 0:
        left_l2 = 11
    if right_l2 == 0:
        right_l2 = 11

    loc = [[0, 0], [0, 1], [0, 2]
        , [1, 0], [1, 1], [1, 2]
        , [2, 0], [2, 1], [2, 2]
        , [3, 0], [3, 1], [3, 2]]

    ldistance = abs(loc[left_l2 - 1][0] - loc[taget - 1][0]) + abs(loc[left_l2 - 1][1] - loc[taget - 1][1])
    rdistance = abs(loc[right_l2 - 1][0] - loc[taget - 1][0]) + abs(loc[right_l2 - 1][1] - loc[taget - 1][1])

    if ldistance > rdistance:
        return 'right'
    elif ldistance < rdistance:
        return 'left'
    else:
        return hand


def solution(numbers, hand):
    answer = ''

    left = [1, 4, 7]
    right = [3, 6, 9]
    left_l = 10
    right_l = 12

    for n in numbers:
        if n in left:
            answer += 'L'
            left_l = n
        elif n in right:
            answer += 'R'
            right_l = n
        else:
            what = cal(n, left_l, right_l, hand)
            if what == 'right':
                right_l = n
                answer += 'R'
            elif what == 'left':
                left_l = n
                answer += 'L'

    return answer